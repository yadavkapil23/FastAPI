#THIS IS CONTROLLER FILE.

from fastapi import APIRouter, HTTPException
from schemas.user import User, CreateUser
#imports the User and CreateUser Pydantic class from user.py file in Schema folder.

router = APIRouter(prefix="/users", tags=["Users"]) #defines an API router.

# In-memory "database"
users_db = []

@router.get("/", response_model=list[User])
def get_users():
    return users_db

#Handles the GET request to /users/ , returns entire list of users stored in users_db.
#It ensures the response is a list of User objects with the id,name and email.


@router.post("/", response_model=User)
def create_user(user: CreateUser):
    new_user = {"id": len(users_db) + 1, **user.model_dump()}
    #it creates a dictionary for the user. , id is set one more that the current no of users to make it unique.
    #users.model_dump() , copies the name and email from the request into the dictionary.

    users_db.append(new_user) #adds the new user to the existing memory.
    return new_user #returns new user.


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")