from fastapi import FastAPI,APIRouter

v1 = APIRouter(prefix= "/v1")

@v1.get("/home")
def home():
    return{""
    "user1" : "KAPIL",
    "user2" : "Naman"
    }