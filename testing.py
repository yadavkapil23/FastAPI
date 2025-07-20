from fastapi import FastAPI,Query,Path,HTTPException
import json

app = FastAPI()

def load_data():
    with open('user.json','r') as f:
        data = json.load(f)

    return data

@app.get("/")
def home():
    return "Welcome to HomePage."

@app.get("/details/{name}")
def get_info(
    name : str = Path(...,description="Username is janesmith.",example="jacksparrow"),
    fullname : str = Query(...,description="Full name is Jane Smith.",example="Jane Smith")):

    data = load_data()
    info = data['users']

    for i in info:
        if i['username'] == name and i['full_name'] == fullname:
            return i
        
    raise HTTPException(status_code=404,detail="User Not Found.")

