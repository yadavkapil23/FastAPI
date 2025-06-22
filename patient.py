from fastapi import FastAPI,Path
import json
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")
def about():
    return {'message':'India is the 4th Largest Economy in the world.'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(...,description='ID of patient in DB',example='P001')):
    
    info = load_data()

    if patient_id in info:
        return info[patient_id]
    return {'error' : 'Patient not found.'}