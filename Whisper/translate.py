from openai import OpenAI
client = OpenAI()

file = open("sample.wav", "rb")
transcript = client.audio.translations.create(
    model="whisper-1",
    file=file,
)

# 챗GPT로 요약
summary = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": f"다음 문장을 한국어로 변역하고 3줄의 글머리 기호로 요약하세요:\n{transcript}"
        }
    ]
)

print(f"요약 결과: \n{summary.choices[0].message.content}")
print(f"요약에 사용한 토큰 수: {summary.usage.total_tokens}")