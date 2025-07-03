#As your FastAPI project grows, writing all endpoints in one file (main.py) becomes messy. To avoid this, APIRouter lets you:
from fastapi import FastAPI,APIRouter

router = APIRouter()

app = FastAPI()

#this is an endpoint directly on the app.
@app.get("/hello")  # -> this will go to the main app file , on route path : /hello .
def home():
    return{
        "message" : "Welcome to our Home."
    }



@router.get("/hello") # -> this will go to the router section , on the route path : /api/hello . 
async def by_router():
    return{
        "message" : "Hello from Router!"
    }

app.include_router(router,prefix="/api")
#This creates a router and adds the /hello route to it.