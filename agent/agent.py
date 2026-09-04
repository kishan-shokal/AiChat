import streamlit as st

from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from .llm import get_llm
from .tools import get_tools


@st.cache_resource
def get_agent():

    llm = get_llm()

    tools = get_tools()

    memory = MemorySaver()

    agent = create_agent(
        model=llm,
        tools=tools,
        checkpointer=memory,
        system_prompt="""
        You are a helpful web research assistant.

        Use the web search tool when the user needs
        current or web-based information.

        Give accurate, clear and concise answers.
        """,
    )

    return agent