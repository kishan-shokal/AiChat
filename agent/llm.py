from langchain_groq import ChatGroq


def get_llm():

    return ChatGroq(
        model="openai/gpt-oss-20b",
        streaming=True,
        temperature=0,
    )