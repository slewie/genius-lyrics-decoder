from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4.1-mini-2025-04-14",
    openai_api_key="unused",
    openai_api_base="https://api.llm7.io/v1",
    temperature=1,
    max_tokens=1000,
)