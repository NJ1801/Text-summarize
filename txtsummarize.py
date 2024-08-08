import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re


def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text


input_file_path = r"C:\Users\MORNING SHIFT\Downloads\excel text.txt"
with open(input_file_path, "r") as file:
    text = file.read()


model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")


preprocessed_text = preprocess_text(text)


input_tokens_before = len(tokenizer(preprocessed_text)['input_ids'])


input_ids = tokenizer.encode("Summarize: " + preprocessed_text, return_tensors='pt', max_length=2048, truncation=True)


summary_ids = model.generate(input_ids, min_length=50, max_length=200, length_penalty=20, num_beams=2)


summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)


print("Generated Summary:", summary)


summary_tokens = len(tokenizer.tokenize(summary))


print("Number of Tokens Before Summarization:", input_tokens_before)
print("Number of Tokens After Summarization:", summary_tokens)