from search import answer_question
from openai import OpenAI
client = OpenAI()

print("질문을 입력하세요")

conversation_history = [{"role": "system", "content": "당신은 내가 키우는 개입니다. 동물의 개가 되어 답변해 주세요. 나를 '주인님'이라고 부르고, 답변의 끝에는 반드시 '강아지'를 붙여주세요."}
]

while True:
    user_input = input()

    if user_input == "exit":
        break

    conversation_history.append({"role": "user", "content": user_input})
    answer = answer_question(user_input, conversation_history)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
    )

    chatgpt_response = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": chatgpt_response})

    print("ChatGPT:", answer)
    conversation_history.append({"role": "assistant", "content": answer})
