from fastapi import FastAPI,HTTPException,Path,Query
import json

app = FastAPI()

def load_data():
    with open('user.json','r') as f:
        data = json.load(f)

    return data

@app.get("/")
def home():
    return "welcome to home page."

@app.get("/details/{name}")
def info(
    name : str = Path(...),
    fullname : str = Query(...)
         ):
    data = load_data()
    information = data['users']

    for i in information:
        if i['username'] == name and i['full_name'] == fullname:
            return i
        
    raise HTTPException(status_code=404,detail="NOt found.")