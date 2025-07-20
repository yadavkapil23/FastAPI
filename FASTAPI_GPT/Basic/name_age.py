from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import List,Dict,Annotated
import json


class details(BaseModel):
    name : str = Field(...,description="Name of Patient",examples=['Naresh','Ramesh'])
    age : int = Field(...,description="Age of student.",examples=[19.37])

app = FastAPI()

@app.post("/user/")
def info(information : details):
    return{
        "message" : f'Name of the Patient is : {information.name} and age is : {information.age}'
    }




