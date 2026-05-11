from fastapi import status, APIRouter
from src.app.Services.Gemma_Embedding import rag_chain
from fastapi.responses import PlainTextResponse
from src.app.Agents.first_agent import agent

llm = APIRouter()

@llm.post("/get_from_llm/", response_class = PlainTextResponse)
async def ask_llm(user_input: str):
    return rag_chain.invoke(user_input)

@llm.post("/get_time/")
async def get_time(user_input: str):
    result = agent.invoke(
    {"messages": [{"role": "user", "content": user_input}]}
    )
    return result["messages"][-1].content

