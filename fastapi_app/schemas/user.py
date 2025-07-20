from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str 
    email : str

class CreateUser(BaseModel):
    #We didn't use the id field in CreateUser because when a new user is created, the client (user of the API) does not provide the id. Instead, the server automatically generates a unique id for each new user
    name : str
    email : str

