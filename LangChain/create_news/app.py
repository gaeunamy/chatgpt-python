from langchain.agents import Tool, create_openai_tools_agent, AgentExecutor
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

def create_prompt():
    template = ChatPromptTemplate.from_messages([
        ("system", "당신은 뉴스 기사를 쓰는 한국의 블로거입니다. 다음 주제에 대해 네이버 검색을 통해 최신 정보를 얻고, 검색된 정보를 바탕으로 리스트를 작성해 한국어로 출력해 주세요. 목록에는 서비스 이름과 '공식 URL', 서비스 개요를 포함시켜 주세요."),
        ("human", "{theme}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])
    return template
    
def define_tools():
    search = GoogleSearchAPIWrapper()
    return [
        Tool(
            name="Serach",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions"
        ),
    ]

def write_response_to_file(response, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response)
    print('출력이 완료되었습니다')

def main():
    llm = ChatOpenAI(temperature=0, model="gpt-4", max_tokens=2000)
    tools = define_tools()
    prompt = create_prompt()

    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_excutor = AgentExecutor(agent=agent, tools=tools)

    response = agent_excutor.invoke({"theme": input("기사 주제를 입력하세요: ")})
    write_response_to_file(response["output"], 'output2.txt')

if __name__ == "__main__":
    main()

