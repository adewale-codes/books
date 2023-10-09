from fastapi import FastAPI
from routers.books import books_router as books_router
from routers.users import router as users_router

app = FastAPI()

app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
def home():
    return {"Welcome to our API application"}
