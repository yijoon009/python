import pandas as pd
from datasets import Dataset, DatasetDict
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          DataCollatorForLanguageModeling, PreTrainedTokenizer,
                          Trainer, TrainingArguments, pipeline)


def tokenize(element, tokenizer=None):
    outputs = tokenizer(
        element["train_input"],
        truncation=True,
        max_length=2048,
        return_overflowing_tokens=False,
        return_length=True,
        padding=True,
    )

    return {"input_ids": outputs["input_ids"]}


def load_data():
    dataset_train = Dataset.from_json("../dataset/holmes_finetune_dataset_train.json")
    dataset_test = Dataset.from_json("../dataset/holmes_finetune_dataset_test.json")
    dataset = DatasetDict({"train": dataset_train, "test": dataset_test})
    return dataset


def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    return tokenizer, model


def preprocess(dataset, tokenizer):
    tokenized_datasets = dataset.map(
        tokenize,
        batched=True,
        remove_columns=dataset["train"].column_names,
        fn_kwargs={"tokenizer": tokenizer},
    )

    data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

    return tokenized_datasets, data_collator


if __name__ == "__main__":
    dataset = load_data()
    tokenizer, model = load_model("../models/camel-5b-hf")
    tokenized_datasets, data_collator = preprocess(dataset, tokenizer)

    save_dir = "../models/camel-5b-finetuned_0331"
    training_params = TrainingArguments(
        output_dir=save_dir,
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=32,
        fp16=True,
        deepspeed="../models/ds_config.json",
    )

    trainer = Trainer(
        model=model,
        tokenizer=tokenizer,
        args=training_params,
        data_collator=data_collator,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
    )

    trainer.train()

    trainer.save_model(output_dir=save_dir)
