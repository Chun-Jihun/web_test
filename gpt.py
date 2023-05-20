from transformers import (
    GPT2Tokenizer,
    DataCollatorForLanguageModeling,
    TextDataset,
    GPT2LMHeadModel,
    TrainingArguments,
    Trainer,
    pipeline)

def solution():
    generator = pipeline('text-generation', tokenizer='gpt2', model='data')
    print(generator('Once upon a time', max_length=40)[0]['generated_text'])