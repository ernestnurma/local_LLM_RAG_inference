from fastapi import status, APIRouter, Query, Path
from typing import Optional, Annotated
from typing import List
from fastapi.exceptions import HTTPException
from src.app.Models.Models import BookModelClass
from src.app.DB.Local_DB import books


book_router = APIRouter()


@book_router.post("/create", status_code=status.HTTP_201_CREATED)
async def post_book(book_data : BookModelClass) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get("/", response_model=List[BookModelClass])
async def get_books() -> list[dict]:
    return books

@book_router.get("/{book_year}")
async def get_a_book(book_year : int):
    for book in books:
        if book["year"] == book_year:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with year {book_year} not found"
    )

@book_router.patch("/update/{book_year}")
async def update_book_info(book_year : int, book_upd_data : BookModelClass):
    for book in books:
        if book["year"] == book_year:
            book["name"] = str(book_upd_data.name),
            book["year"] = int(book_upd_data.year)

            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with year {book_year} not found. Can't upgrate "
    )

@book_router.delete("/{book_year}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_year : int):
    for book in books:
        if book["year"] == book_year:
            books.remove(book)
            return {}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with year {book_year} not found"
    )
