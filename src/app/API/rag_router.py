from fastapi import status, APIRouter
from src.app.Services.Gemma_Embedding import rag_chain
from fastapi.responses import PlainTextResponse
llm = APIRouter()

@llm.post("/get_from_llm/", response_class = PlainTextResponse)
async def ask_llm(user_input: str):
    return rag_chain.invoke(user_input)