from openai import OpenAI
client = OpenAI()

def make_tweet():
    request = "저는 IT 관련 기업에 근무하는 입사 1년차 신입사원입니다. 저를 대신해 트위터에 올릴 트윗을 140자 이내로 작성해 주세요. \n\n 트윗을 작성할 때 다음 예문을 참고해 주세요.\n\n"
    tweet1 = "예문1: 직장에서 파이썬을 사용하게 될 것 같아서 현재 공부 중입니다! 프로그래밍이라던가 어려워서 잘 모르겠어..\n\n"
    tweet2 = "예문2: 최근에 ChatGPT에 대해 여러 가지를 알아보고 있는데, 어떤 질문에도 대답해줘서 정말 대단하네요! 일단 Python으로 간단한 대화를 하는 프로그램을 작성해 볼 생각이에요. 잘 할 수 있을까\n\n"

    content = request + tweet1 + tweet2

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 매우 낙천적인 성격입니다. 또 말끝을 '~인 것이다'로 끝맺는 버릇이 있습니다."},
            {"role": "user", "content": limited_content},
        ],
    )

    return response.choices[0].message.content
