from fastapi import FastAPI
from src.app.API.book_router import book_router
from src.app.API.rag_router import llm


version = "v1"

app = FastAPI(
    version= version
)

app.include_router(
    book_router,
    prefix=f"/api/{version}/books"
)
app.include_router(
    llm,
    prefix="/api/llm"
)
