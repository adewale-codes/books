from fastapi import APIRouter

router = APIRouter()

fake_users = [
    {
        "username": "johndoe",
        "age": 25,

    }
]

@router.get("/")
def get_users():
    return fake_users