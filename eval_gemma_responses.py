from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

PLAYER_FORECAST_JSON_EXAMPLE = """Format example:
{
  "predicted_points_1gw": 4.0,
  "predicted_points_3gw": 12.0,
  "predicted_points_5gw": 19.0,
  "predicted_minutes_1gw": 86.0,
  "predicted_appearance_probability": 0.94
}
Output exactly one JSON object in that shape and nothing else."""

PLAYER_FORECAST_DELTA_JSON_EXAMPLE = """Format example:
{
  "delta_points_1gw": -0.5,
  "delta_points_3gw": 1.2,
  "delta_points_5gw": 2.0,
  "delta_minutes_1gw": -8.0,
  "delta_appearance_probability": -0.1
}
Output exactly one JSON object in that shape and nothing else."""

TRANSFER_CHOICE_JSON_EXAMPLE = """Format example:
{
  "selected_option": 1,
  "reasoning_summary": [
    "The option improves projected score while staying within the legal candidate set.",
    "The captaincy and lineup remain aligned with the strongest structured forecasts."
  ]
}
Output exactly one JSON object in that shape and nothing else."""


def load_examples(path: Path):
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def build_prompt(tokenizer, messages):
    prompt_messages = [m for m in messages if m.get("role") in {"system", "user"}]
    if prompt_messages:
        last_message = prompt_messages[-1]
        user_content = str(last_message.get("content", ""))
        if "predicted_points_1gw" in user_content and "Return exactly one JSON object" in user_content:
            last_message = dict(last_message)
            last_message["content"] = user_content.rstrip() + "\n\n" + PLAYER_FORECAST_JSON_EXAMPLE
            prompt_messages = [*prompt_messages[:-1], last_message]
        elif "delta_points_1gw" in user_content and "Return exactly one JSON object" in user_content:
            last_message = dict(last_message)
            last_message["content"] = user_content.rstrip() + "\n\n" + PLAYER_FORECAST_DELTA_JSON_EXAMPLE
            prompt_messages = [*prompt_messages[:-1], last_message]
        elif "selected_option" in user_content and "Return strict JSON" in user_content:
            last_message = dict(last_message)
            last_message["content"] = user_content.rstrip() + "\n\n" + TRANSFER_CHOICE_JSON_EXAMPLE
            prompt_messages = [*prompt_messages[:-1], last_message]
    return tokenizer.apply_chat_template(
        prompt_messages,
        tokenize=False,
        add_generation_prompt=True,
    )


def build_prompt_from_example(tokenizer, example):
    if "prompt" in example:
        return example["prompt"]
    return build_prompt(tokenizer, example["messages"])


def generate_responses(model, tokenizer, prompts: list[str], max_new_tokens: int):
    # Left padding so every sequence ends at the same position and decode
    # steps stay aligned across the batch.
    tokenizer.padding_side = "left"
    inputs = tokenizer(prompts, return_tensors="pt", padding=True)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    if "input_ids" in inputs:
        inputs["mm_token_type_ids"] = torch.zeros_like(inputs["input_ids"])
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=None,
            top_p=None,
            top_k=None,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
        )
    prompt_length = inputs["input_ids"].shape[1]
    return [
        tokenizer.decode(sequence[prompt_length:], skip_special_tokens=True).strip()
        for sequence in output
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-path', required=True)
    parser.add_argument('--examples', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--adapter-path', default=None)
    parser.add_argument('--max-new-tokens', type=int, default=512)
    parser.add_argument('--no-4bit', action='store_true', help='Load in bf16 without bitsandbytes quantization (default for small models like E4B).')
    parser.add_argument('--batch-size', type=int, default=1, help='Prompts generated together (left-padded). Decode at batch 1 leaves the GPU idle; 16 is safe on the GB10 at ~1k-token prompts.')
    parser.add_argument('--resume', action='store_true', help='Append to an existing output file, skipping as many examples as it already has rows.')
    parser.add_argument('--no-merge', action='store_true', help='Keep the LoRA adapter unmerged (slow; merged decoding is identical).')
    args = parser.parse_args()

    model_path = Path(args.model_path)
    examples_path = Path(args.examples)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, extra_special_tokens={})
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model_kwargs = dict(
        torch_dtype=torch.bfloat16,
        device_map='auto',
        trust_remote_code=True,
        attn_implementation='sdpa',
    )
    if not args.no_4bit:
        model_kwargs['quantization_config'] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type='nf4',
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

    model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)
    model.eval()

    if args.adapter_path:
        model = PeftModel.from_pretrained(model, args.adapter_path)
        # Our adapters are target_parameters LoRA, which rebuilds every wrapped weight on each
        # forward call: ~1.4 s per decode step on the GB10. Merging once gives identical outputs
        # (max |dP| 0.0 on E20, 2026-10-09) and ~9x faster decode steps.
        if not args.no_merge:
            try:
                model = model.merge_and_unload()
            except Exception as exc:  # a slow decode beats a failed live decode
                print(f"adapter merge failed ({exc}); decoding unmerged")
        model.eval()

    skip = 0
    if args.resume and output_path.exists():
        with output_path.open() as handle:
            skip = sum(1 for line in handle if line.strip())
        print(f"resuming: skipping {skip} examples already generated")

    examples = list(load_examples(examples_path))[skip:]
    with output_path.open('a' if args.resume else 'w') as handle:
        for start in range(0, len(examples), args.batch_size):
            batch = examples[start:start + args.batch_size]
            prompts = [build_prompt_from_example(tokenizer, example) for example in batch]
            responses = generate_responses(model, tokenizer, prompts, args.max_new_tokens)
            for example, response in zip(batch, responses):
                record = {
                    'season': example['season'],
                    'week': example['week'],
                    'response': response,
                }
                if 'metadata' in example:
                    record['metadata'] = example['metadata']
                handle.write(json.dumps(record) + "\n")
            handle.flush()
            last = batch[-1]
            print(f"generated {skip + start + len(batch)}/{skip + len(examples)} (thru {last['season']} GW{last['week']})")


if __name__ == '__main__':
    main()
