from fastapi import FastAPI,APIRouter

user_router = APIRouter(
    prefix="/kapil",
    tags=['kapil'],
    responses={404: {"description": "Not found"}} #we can also set the custom values for all routes.
    )

app = FastAPI()


users_db = {1: "Alice", 2: "Bob"}

@app.get("/home")
def home():
    return{
        "message" : "Welcome Buddy!"
    }

@user_router.get("/home")
async def basic():
    return users_db

# @user_router.get("/{user_id}")
# def details(user_id : int):
#     return{
#         "user_id" : user_id
#     }

@user_router.get("/{user_id}")
def get_by_id( user_id : int):
    name = users_db.get(user_id)
    if name is None:
        return{"Error":"Not Found."}

    return{
        "user_id" : user_id,
        "name" : name
    }

app.include_router(user_router)