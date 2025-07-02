#Create a PATCH endpoint /user/{user_id} to partially update a user's email. Only the email field should be optional in the request body.

from fastapi import FastAPI,HTTPException
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

users_db = {
    1: {"name": "John Doe", "email": "john@example.com"},
    2: {"name": "William Edward", "email": "william@xmail.com"}
}

class Update(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None

@app.patch("/user/{user_id}")
async def update(user_id : str , user_obj = Update):
    
    if user_id not in users_db:
        raise HTTPException(status_code=404,detail="Not found.")
    if user_obj.email not in users_db:
        users_db[user_id]['email'] = user_obj.email
    return JSONResponse(content="Done Successfully.")
    