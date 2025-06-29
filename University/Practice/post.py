from fastapi import FastAPI,HTTPException,Path,Query
from typing import Optional,Annotated
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
import json

app = FastAPI()


class Student(BaseModel):
    id : Annotated[str, Field(..., description="ID of student", examples=["CSE001"])]
    name : Annotated[str, Field(..., description="Name of Student", examples=["Naman Sharma"])]
    department : Annotated[str, Field(..., description="Department name", examples=["CSE"])]
    year : Annotated[int, Field(..., description="Year of student", examples=[1])]
    gender : Annotated[str, Field(..., description="Gender of the student", examples=["male"])]
    city : Annotated[str, Field(..., description="City of student", examples=["New Delhi"])]
    cgpa : Annotated[float, Field(..., description="CGPA of student", examples=[7.8])]
    
class UpdatedStudent(BaseModel):
    id : Annotated[Optional[str], Field(None, description="ID of student", examples=["CSE001"])]
    name : Annotated[Optional[str], Field(None, description="Name of Student", examples=["Naman Sharma"])]
    department : Annotated[Optional[str], Field(None, description="Department name", examples=["CSE"])]
    year : Annotated[Optional[int], Field(None, description="Year of student", examples=[1])]
    gender : Annotated[Optional[str], Field(None, description="Gender of the student", examples=["male"])]
    city : Annotated[Optional[str], Field(None, description="City of student", examples=["New Delhi"])]
    cgpa : Annotated[Optional[float], Field(None, description="CGPA of student", examples=[7.8])]



def save_data(data):
    with open('students.json','w') as f:
        json.dump(data,f)


def load_data():
    with open('students.json','r') as f:
        data = json.load(f)
        return data
    
@app.get("/")
def home():
    return "Welcome to HomePage."

#if you want to get the student with the ID , then
@app.get("/details/{student_id}")
def get_details(student_id : str = Path()):
    data = load_data()

    if student_id in data:
        return data[student_id]
    raise HTTPException(status_code=404,detail="Student Not Found In Records.")

