from pathlib import Path
import inspect
import os
import json

import torch
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, prepare_model_for_kbit_training
from trl import SFTConfig, SFTTrainer
from trl.trainer.sft_trainer import DataCollatorForLanguageModeling

ROOT = Path(__file__).resolve().parent
MODEL_PATH = os.environ.get("FPL_GEMMA_MODEL_PATH", "/home/wescheng/models/gemma-4-31b-it")
LOAD_IN_4BIT = os.environ.get("FPL_GEMMA_LOAD_IN_4BIT", "true").lower() in {"1", "true", "yes", "on"}
DATA_DIR = Path(os.environ.get("FPL_GEMMA_DATA_DIR", ROOT / "reports" / "llm_sft_split_2025_26_gw11_30"))
TRAIN_PATH = DATA_DIR / "train.jsonl"
EVAL_PATH = DATA_DIR / "eval.jsonl"
OUTPUT_DIR = Path(
    os.environ.get("FPL_GEMMA_OUTPUT_DIR", ROOT / "artifacts" / "gemma4_31b_lora_squad_v2_textonly")
)
RESUME_FROM_CHECKPOINT = os.environ.get("FPL_GEMMA_RESUME_FROM_CHECKPOINT")
MAX_SEQ_LENGTH = int(os.environ.get("FPL_GEMMA_MAX_SEQ_LENGTH", "2048"))
TRUNCATION_MODE = os.environ.get("FPL_GEMMA_TRUNCATION_MODE", "keep_start")
MAX_STEPS = int(os.environ.get("FPL_GEMMA_MAX_STEPS", "-1"))
NUM_EPOCHS = float(os.environ.get("FPL_GEMMA_NUM_EPOCHS", "1"))
LEARNING_RATE = float(os.environ.get("FPL_GEMMA_LEARNING_RATE", "1e-4"))
TRAIN_BATCH_SIZE = int(os.environ.get("FPL_GEMMA_TRAIN_BATCH_SIZE", "1"))
EVAL_BATCH_SIZE = int(os.environ.get("FPL_GEMMA_EVAL_BATCH_SIZE", "1"))
GRADIENT_ACCUMULATION_STEPS = int(os.environ.get("FPL_GEMMA_GRAD_ACCUM", "16"))
LOGGING_STEPS = int(os.environ.get("FPL_GEMMA_LOGGING_STEPS", "5"))
EVAL_STEPS = int(os.environ.get("FPL_GEMMA_EVAL_STEPS", "20"))
SAVE_STEPS = int(os.environ.get("FPL_GEMMA_SAVE_STEPS", "20"))
SAVE_TOTAL_LIMIT = int(os.environ.get("FPL_GEMMA_SAVE_TOTAL_LIMIT", "2"))
WARMUP_STEPS = int(os.environ.get("FPL_GEMMA_WARMUP_STEPS", "5"))
EVAL_STRATEGY = os.environ.get("FPL_GEMMA_EVAL_STRATEGY", "steps")
SAVE_STRATEGY = os.environ.get("FPL_GEMMA_SAVE_STRATEGY", "steps")
COMPLETION_ONLY_LOSS = os.environ.get("FPL_GEMMA_COMPLETION_ONLY_LOSS")
GRADIENT_CHECKPOINTING = os.environ.get("FPL_GEMMA_GRADIENT_CHECKPOINTING", "true").lower() in {
    "1",
    "true",
    "yes",
    "on",
}
LORA_R = int(os.environ.get("FPL_GEMMA_LORA_R", "16"))
LORA_ALPHA = int(os.environ.get("FPL_GEMMA_LORA_ALPHA", "32"))
LORA_DROPOUT = float(os.environ.get("FPL_GEMMA_LORA_DROPOUT", "0.05"))
DEFAULT_TARGET_SUFFIXES = (
    "self_attn.q_proj.weight",
    "self_attn.k_proj.weight",
    "self_attn.v_proj.weight",
    "self_attn.o_proj.weight",
    "mlp.gate_proj.weight",
    "mlp.up_proj.weight",
    "mlp.down_proj.weight",
)
TARGET_SUFFIXES = tuple(
    suffix.strip()
    for suffix in os.environ.get("FPL_GEMMA_TARGET_SUFFIXES", ",".join(DEFAULT_TARGET_SUFFIXES)).split(",")
    if suffix.strip()
)


def format_example(example):
    if "prompt" in example and "completion" in example:
        return {
            "prompt": example["prompt"],
            "completion": example["completion"],
        }
    messages = example["messages"]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=False,
    )
    return {"text": text}


def make_text_only_gemma4_collator(tokenizer, needs_mm_token_type_ids):
    completion_only_loss = True
    if COMPLETION_ONLY_LOSS is not None:
        completion_only_loss = COMPLETION_ONLY_LOSS.lower() in {"1", "true", "yes", "on"}
    base_collator = DataCollatorForLanguageModeling(
        pad_token_id=tokenizer.pad_token_id,
        completion_only_loss=completion_only_loss,
    )

    def collate(features):
        batch = base_collator(features)
        if needs_mm_token_type_ids:
            batch["mm_token_type_ids"] = torch.zeros_like(batch["input_ids"])
        return batch

    return collate


LANGUAGE_MODEL_LAYER_PREFIXES = (
    "model.language_model.layers.",
    "model.layers.",
)


def find_language_model_target_parameters(model):
    for prefix in LANGUAGE_MODEL_LAYER_PREFIXES:
        target_parameters = sorted(
            name
            for name, _ in model.named_parameters()
            if name.startswith(prefix) and any(name.endswith(suffix) for suffix in TARGET_SUFFIXES)
        )
        if target_parameters:
            return target_parameters

    raise RuntimeError("No Gemma language-model target parameters were found for LoRA.")


def load_jsonl_dataset(path: Path) -> Dataset:
    rows = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return Dataset.from_list(rows)


def dataset_mode(dataset: Dataset) -> str:
    sample = next(iter(dataset))
    if "prompt" in sample and "completion" in sample:
        return "prompt_completion"
    if "messages" in sample:
        return "messages"
    raise ValueError("Expected JSONL rows to contain either prompt/completion or messages.")


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True, extra_special_tokens={})
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model_kwargs = dict(
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
        attn_implementation="sdpa",
    )
    if LOAD_IN_4BIT:
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, **model_kwargs)
    model.config.use_cache = False
    if LOAD_IN_4BIT:
        model = prepare_model_for_kbit_training(model)
    target_parameters = find_language_model_target_parameters(model)
    print(f"Targeting {len(target_parameters)} language-model parameters for LoRA")

    train_ds = load_jsonl_dataset(TRAIN_PATH)
    eval_ds = load_jsonl_dataset(EVAL_PATH)
    mode = dataset_mode(train_ds)
    if dataset_mode(eval_ds) != mode:
        raise ValueError("Train and eval datasets must use the same row format.")
    print(f"Dataset mode: {mode}")

    if mode == "messages":
        train_ds = train_ds.map(format_example, remove_columns=train_ds.column_names)
        eval_ds = eval_ds.map(format_example, remove_columns=eval_ds.column_names)

    peft_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=None,
        target_parameters=target_parameters,
    )

    training_args = SFTConfig(
        output_dir=str(OUTPUT_DIR),
        per_device_train_batch_size=TRAIN_BATCH_SIZE,
        per_device_eval_batch_size=EVAL_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        learning_rate=LEARNING_RATE,
        num_train_epochs=NUM_EPOCHS,
        max_steps=MAX_STEPS,
        logging_steps=LOGGING_STEPS,
        eval_strategy=EVAL_STRATEGY,
        eval_steps=EVAL_STEPS,
        save_strategy=SAVE_STRATEGY,
        save_steps=SAVE_STEPS,
        save_total_limit=SAVE_TOTAL_LIMIT,
        bf16=True,
        gradient_checkpointing=GRADIENT_CHECKPOINTING,
        warmup_steps=WARMUP_STEPS,
        lr_scheduler_type="cosine",
        weight_decay=0.0,
        report_to="none",
        dataset_text_field="text",
        packing=False,
        max_length=MAX_SEQ_LENGTH,
        truncation_mode=TRUNCATION_MODE,
        completion_only_loss=COMPLETION_ONLY_LOSS.lower() in {"1", "true", "yes", "on"}
        if COMPLETION_ONLY_LOSS is not None
        else None,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        peft_config=peft_config,
        processing_class=tokenizer,
        data_collator=make_text_only_gemma4_collator(
            tokenizer,
            needs_mm_token_type_ids="mm_token_type_ids" in inspect.signature(model.forward).parameters,
        ),
    )

    trainer.train(resume_from_checkpoint=RESUME_FROM_CHECKPOINT)
    trainer.save_model(str(OUTPUT_DIR))
    tokenizer.save_pretrained(str(OUTPUT_DIR))
