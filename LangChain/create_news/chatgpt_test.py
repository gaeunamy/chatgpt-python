from openai import OpenAI
client = OpenAI()

# 챗GPT API를 통해 요청을 보내고 결과를 가져옴
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Python에 대해 알려주세요"},
    ],
)

# API의 응답에서 답변 부분만 표시
print(response.choices[0].message.content)