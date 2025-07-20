#Write a PUT endpoint /user/{user_id} that updates a user's name and email.

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()

users_db = {
    1: {"name": "John Doe", "email": "john@example.com"},
    2: {"name": "Jane Doe", "email": "jane@example.com"}
}

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


@app.get("/info")
def show():
    return{
        'message' : 'welcome to homepage'
    }


@app.put("/user/{user_id}")
async def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    if user_update.name is not None:
        users_db[user_id]["name"] = user_update.name
    if user_update.email is not None:
        users_db[user_id]["email"] = user_update.email
    return {"user_id": user_id, "updated_user": users_db[user_id]}
