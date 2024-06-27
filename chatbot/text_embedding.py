import pandas as pd
import tiktoken
from openai import OpenAI
from typing import List

client = OpenAI()

embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
max_tokens = 1500

df = pd.read_csv("scraped.csv")
df.columns = ['title', 'text']

tokenizer = tiktoken.get_encoding(embedding_encoding)
df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))

# 텍스트를 최대 토큰 수로 나누는 함수
def split_into_many (text, max_tokens = 500):
    sentences = text.split('.')
    n_tokens = [len(tokenizer.encode(" " + sentence)) for sentence in sentences]

    chunks = []
    tokens_so_far = 0
    chunk = []

    for sentence, token in zip(sentences, n_tokens):
        if tokens_so_far + toekn > max_tokens:
            chunks.append(". ".join(chunk) + ".")
            chunk = []
            tokens_so_far

        if token > max_tokens:
            continue

        chunk.append(sentence)
        tokens_so_far += token + 1

    if chunk:
        chunks.append(". ".join(chunk) + ".")
    return chunks

shortend = []

for row in df.iterrows():
    if row[1]['text'] is None:
        continue

    if row[1]['n_tokens'] > max_tokens:
        shortend += split_into_many(row[1]['text'])

    else:
        shortend.append(row[1]['text'])

df = pd.DataFrame(shortend, columns = ['text'])

df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))

def get_embedding(text, model):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

df["embeddings"] = df.text.apply(lambda x: get_embedding(x, model=embedding_model))
df.to_csv('embedding.csv')