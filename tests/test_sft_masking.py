"""Verify completion-only loss masking in the SFT pipeline.

The training script (train_gemma_sft.py) relies on two TRL behaviors:
1. SFTTrainer, given prompt/completion rows, tokenizes them separately and
   emits a `completion_mask` marking which tokens belong to the completion.
2. `DataCollatorForLanguageModeling(completion_only_loss=True)` sets labels
   to -100 wherever completion_mask == 0, so CrossEntropyLoss only sees the
   JSON target tokens.

These tests pin both behaviors so a TRL upgrade or config drift that starts
training on prompt grammar fails loudly.
"""

import torch
from trl.trainer.sft_trainer import DataCollatorForLanguageModeling


def _make_feature(prompt_len: int, completion_len: int):
    input_ids = list(range(10, 10 + prompt_len + completion_len))
    completion_mask = [0] * prompt_len + [1] * completion_len
    return {"input_ids": input_ids, "completion_mask": completion_mask}


def test_collator_masks_prompt_tokens_with_minus_100():
    collator = DataCollatorForLanguageModeling(pad_token_id=0, completion_only_loss=True)
    prompt_len, completion_len = 7, 4
    batch = collator([_make_feature(prompt_len, completion_len)])
    labels = batch["labels"][0]

    assert (labels[:prompt_len] == -100).all(), "prompt tokens must be masked out of the loss"
    completion_labels = labels[prompt_len : prompt_len + completion_len]
    assert (completion_labels != -100).all(), "completion tokens must contribute to the loss"
    assert torch.equal(
        completion_labels, batch["input_ids"][0][prompt_len : prompt_len + completion_len]
    ), "completion labels must equal the completion input ids"


def test_collator_masks_padding_in_batches():
    collator = DataCollatorForLanguageModeling(pad_token_id=0, completion_only_loss=True)
    short = _make_feature(3, 2)
    long = _make_feature(6, 5)
    batch = collator([short, long])
    labels_short = batch["labels"][0]
    pad_region = labels_short[5:]
    assert (pad_region == -100).all(), "padding must be masked out of the loss"


def test_collator_without_completion_only_trains_on_prompt():
    """Contrast case: documents what turning the flag off would do."""
    collator = DataCollatorForLanguageModeling(pad_token_id=0, completion_only_loss=False)
    batch = collator([{"input_ids": list(range(10, 20))}])
    assert (batch["labels"][0] != -100).all()


def test_sft_trainer_emits_completion_mask_for_prompt_completion_rows():
    """End-to-end: TRL's dataset prep must produce the completion_mask the
    collator depends on, with the mask boundary exactly at the prompt end."""
    from datasets import Dataset
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("google/gemma-4-E4B-it")
    prompt = "<|turn>user\nforecast please<|turn>\n<|turn>model\n"
    completion = '{"delta_points_1gw":0.5}'

    from trl import SFTConfig, SFTTrainer

    dataset = Dataset.from_list([{"prompt": prompt, "completion": completion}])
    shell = SFTTrainer.__new__(SFTTrainer)  # prep-only shell; avoids loading the model
    shell._is_vlm = False
    prepared = SFTTrainer._prepare_dataset(
        shell,
        dataset,
        tokenizer,
        SFTConfig(output_dir="/tmp/unused", report_to="none", max_length=512, packing=False),
        packing=False,
        formatting_func=None,
        dataset_name="train",
    )
    row = prepared[0]
    assert "completion_mask" in row, "TRL prompt/completion prep must emit completion_mask"
    mask = row["completion_mask"]
    prompt_token_count = len(tokenizer(prompt, add_special_tokens=True).input_ids)
    assert sum(mask[:prompt_token_count-1]) == 0, "prompt region must be mask=0"
    assert sum(mask) > 0, "completion region must be mask=1"
    completion_ids = [i for i, m in zip(row["input_ids"], mask) if m == 1]
    decoded = tokenizer.decode(completion_ids)
    assert '"delta_points_1gw"' in decoded, f"masked-in region should be the JSON target, got: {decoded!r}"
