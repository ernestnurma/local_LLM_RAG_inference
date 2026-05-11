from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from src.app.Tools.tools import *


# 1. Initialize the Model (ensure Llama 3.1 is pulled in Ollama)
llm = ChatOllama(model="llama3.1", temperature=0)


# Use this instead of create_tool_calling_agent
agent = create_agent(
    model=llm,
    tools=[get_currecnt_time],
    system_prompt="You are a helpful assistant."
)

#