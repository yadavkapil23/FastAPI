from fastapi import FastAPI,Path,HTTPException,Query
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
    raise HTTPException(status_code=404,detail="Patient Not Found.")

@app.get('/sort')
def sort_patients(sort_by : str = Query(...,description="Sort on the basis of height , weight"), order:str = Query('asc',description='sort in ascending or descending order')):
    validfields = ['height','weights']
    if sort_by not in validfields:
        raise HTTPException(status_code=400,detail=f'invalid field select from {validfields}')
    
    if order not in ['asc','dsc']:
        raise HTTPException(status_code=400,detail="Invalid order select between asc and dsc.")
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(),key=lambda x : x.get(sort_by,0),reverse=False)

    return sorted_data