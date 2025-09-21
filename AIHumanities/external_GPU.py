from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# llm = OllamaLLM(
#     base_url="http://localhost:11434",
#     model="gemma3:12b",
# )

# response = llm.invoke("장곡사 미륵불 괘불탱에 대해 설명해줘.")
# print(response)


llm = ChatOllama(
    base_url="http://localhost:11434",  # ollama serve가 켜져 있는 주소
    model="gemma3:12b",
    temperature=0.1,
    num_ctx=2048,
) 

resp = llm.invoke([
    SystemMessage(content="너는 AI 문화유산 스마트도슨트야."),
    HumanMessage(content="장곡사 미륵불 괘불탱에 대해서 설명해줘."),
])
print(resp.content)