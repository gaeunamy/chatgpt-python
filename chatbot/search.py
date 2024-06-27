import pandas as pd 
from openai import OpenAI
import numpy as np 
from typing import List
from scipy import spatial

client = OpenAI()

def create_context(question, df, max_len=1800):
    q_embeddings = client.embeddings.create(input=[question], model='text-embedding-3-small').data[0].embedding
    
    df['distances'] = distances_from_embeddings(q_embeddings, df['embeddings'].apply(eval).apply(np.array).values, distance_metric='cosine')

    returns = []
    
    cur_len = 0

    for _, row in df.sort_values('distances', ascending=True).iterrows():
        cur_len += row['n_tokens'] + 4

        if cur_len > max_len:
            break
        
        returns.append(row["text"])

    return "\n\n###\n\n".join(returns)

def answer_question(question, conversation_history):
    df = pd.read_csv('embedding.csv')

    context = create_context(question, df, max_len=200)

    prompt = f"당신은 어느 호텔 직웝입니다. 문맥에 따라 고객의 질문에 정중하게 대답해 주십시오. 컨텍스트가 질문에 대답할 수 없는 경우 '모르겠습니다'라고 대답하세요. \n\n컨텍스트: {context}\n\n---\n\n질문: {question}\n답변:"
    conversation_history.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=1,
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        print(e)
        return ""

def distances_from_embeddings(
    query_embedding: List[float],
    embeddings: List[List[float]],
    distance_metric="cosine",
) -> List[List]:
    distance_metrics = {
        "cosine": spatial.distance.cosine,
        "L1": spatial.distance.cityblock,
        "L2": spatial.distance.euclidean,
        "Linf": spatial.distance.chebyshev,
    }
    distances = [
        distance_metrics[distance_metric](query_embedding, embedding)
        for embedding in embeddings
    ]
    return distances