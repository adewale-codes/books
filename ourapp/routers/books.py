from fastapi import APIRouter

books_router = APIRouter()

fake_books = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
    },
    {
        "title": "Harry Potter and the chamber of Secrets",
        "author": "Adewale Abiola"
    }
]

@books_router.get("/")
def get_books():
    return fake_books

@books_router.get("/{author}")
def get_books(author: str):
    for book in fake_books:
        if book["author"] == author:
            return book
    return {"error": "Author not found"}