from fastapi import FastAPI,APIRouter

v1_router = APIRouter(prefix= "/v1")

@v1_router.get("/home")
def home():
    return{""
    "user1" : "KAPIL",
    "user2" : "Naman"
    }