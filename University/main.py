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

@app.get("/show")
def show():
    data = load_data()

    return data

#if you want to get the student with the ID , then
@app.get("/details/{student_id}")
def get_details(student_id : str = Path()):
    data = load_data()

    if student_id in data:
        return data[student_id]
    raise HTTPException(status_code=404,detail="Student Not Found In Records.")


#if we want to get according to the year then
@app.get("/info")
def get_by_year(
    year : int = Query(default=None)): #if year is not provided its value is none.
    data = load_data()

    result = {} #initializes a dictionary to store the data of filtered students.

    if not year == None: #to check is year is provided or not.
            for key,student in data.items(): #iterated over each item in the data , here key is students ID , and student is the dictionary containing the details.
             if student.get('year') == year: #check if the student detail matches the year provided in query.
              result[key] = student #if matches , adds student to result dictionary

    else:   #if year was not provided
        result = data #give result of all students.

    if not result:
        raise HTTPException(status_code=404,detail="Not found.") #if the result dictionary is empy , raise an error.
    
    return result #returns dictionary.




    
# GET /students → Returns all students
# GET /students?year=2 → Returns only 2nd year students
# If ?year= is not provided, the API will throw a 422 error.
# Because it’s required (... means required).

@app.get("/credentials")
def get_by_gender(
    gender : str = Query(default="Others")
):
    data = load_data()
    output = {}

    if not gender == "Others":
        for key,student in data.items():
            if student.get('gender') == gender:
                output[key] = student
    else:
        output = data

    if not output:
        raise HTTPException(status_code=400,detail="Not found.")
    
    return output
                

@app.post("/create")
def create_student(student : Student): #here we have created a variable student to store the data from the incoming request body , and it is of type Student.
    data = load_data()

    if student.id in data:
        raise HTTPException(status_code=400,detail="Student already exists in data.")
    
    #if not then create
    data[student.id] = student.model_dump(exclude=['id']) #we are excluding id beacuse we have already used it as key in out dictioanry.


#if included our data would look like - 
#     {
#   "CSE001": {
#     "id": "CSE001",
#     "name": "Naman Sharma",
#     ...
#   }
# }

    #save data
    save_data(data)

    return JSONResponse(status_code=201,content="Saved successfully.")




#DELETE
@app.delete("/delete/{student_id}")
def delete_student(student_id : str):
    data = load_data()

    if student_id not in data:
        raise HTTPException(status_code=400,detail="Student Not found.")
    
    del data[student_id]

    save_data(data)

    return JSONResponse(status_code=201,content="Deleted Successfully.")


#PUT
@app.put("/edit/{student_id}")
def update(student_id : str , student_update : Student):
    data = load_data()

    if student_update.id not in data:
        raise HTTPException(status_code=401,detail="Student not found.")
    
    existing_Student_info = data[student_id]

    updated_student_info =student_update.model_dump(exclude_unset=True)

    for key,value in updated_student_info.items():
        existing_Student_info[key] = value


    existing_Student_info['id'] = student_id

    student_pydantic_object = Student(**existing_Student_info)

    existing_Student_info = student_pydantic_object.model_dump(exclude='id')

    data[student_id] = existing_Student_info

    save_data(data)
    