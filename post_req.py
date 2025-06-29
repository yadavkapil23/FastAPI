from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse


import json
app = FastAPI()


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the Patient", examples=['P001'])]
    name: Annotated[str, Field(..., description="Name of the Patient", examples=["Naman Kumar"])]
    city: Annotated[str, Field(..., description="City of Patient", examples=["New Delhi"])]
    age: Annotated[int, Field(..., gt=0, le=120, description="Age of Patient", examples=[19])]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="Gender of Patient", examples=["male"])]
    height: Annotated[float, Field(..., gt=0, description="Height of Patient in feet", examples=[6.1])]
    weight: Annotated[float, Field(..., gt=0, description="Weight of Patient", examples=[78])]

    @computed_field
    @property
    def bmi(self) -> float:
        height_m = self.height * 0.3048
        return round(self.weight / (height_m ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Lower Obese"
        else:
            return "High Obese"

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data


def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')



@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), 
    order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi'] #the user will send any one field from thse and it will sort accordingly.

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data



@app.post('/create')
def create_patient(patient : Patient): #here we will receive the data coming in a variable patient , and us variable ka data type hoga Hmara pydantic model(Patient)
    #mtlab yha par ham apna data pydantic model ki help se validate krenge

    #load existing data
    data = load_data()

    #check if patient already exists.
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient Already Exists.")
    
    #new patient add to the database.
    data[patient.id] = patient.model_dump(exclude=['id'])


    #saving the data
    save_data(data)

    return JSONResponse(status_code=201,content="Successfully created.")