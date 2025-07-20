from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
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

    @property
    def bmi(self) -> float:
        height_m = self.height * 0.3048
        return round(self.weight / (height_m ** 2), 2)

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
        



class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(..., description="Name of the Patient", examples=["Naman Kumar"])]
    city: Annotated[Optional[str], Field(..., description="City of Patient", examples=["New Delhi"])]
    age: Annotated[Optional[int], Field(..., gt=0, le=120, description="Age of Patient", examples=[19])]
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(..., description="Gender of Patient", examples=["male"])]
    height: Annotated[Optional[float], Field(..., gt=0, description="Height of Patient in feet", examples=[6.1])]
    weight: Annotated[Optional[float], Field(..., gt=0, description="Weight of Patient", examples=[78])]





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



@app.put('/edit/{patient_id}')
def update_patient(patient_id : str , patient_update : PatientUpdate): #here patient_update is a variable used to store the data in the incoming request body and it is of pydantic model type.

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found.")
    
    existing_patient_info = data[patient_id] #extracting the information of existing patient from the data using the patiend id.


     #ab jo patient_update h or jo existing_patient_info h , dono ko dictionary me convert krte h , to dono k saath kaam krna easy ho jaaega.
     #because jo existing_patient_info h , vo hmare database m uski details h , and jo request body k through jo data aa rha h ,update krne k liye , vo hmare existing me hi update krega, so it would be easier , if both are of same type.

    updated_patient_info = patient_update.model_dump(exclude_unset=True)  #here agar ham exclude_unset na likhte to baaki saari fields b dictionary me aa jaati bhale hi saari optional ho.
    #isse sirf vo hi fields dictionary me convert hongi jo ki aayi h.

    #loop chla rhe h and key or value dono ko extract kar rhe h.
    for key,value in updated_patient_info.items():
        existing_patient_info[key] = value


    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id


    patient_pydandic_obj = Patient(**existing_patient_info)


    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    data[patient_id] = existing_patient_info

    save_data(data)

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})

