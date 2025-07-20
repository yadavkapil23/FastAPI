from fastapi import FastAPI,Path,HTTPException
import json

app = FastAPI()

def load_data():
    with open('cars.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def home():
    return "Welcome to our Our System."

@app.get("/info")
def info():
    infor = load_data()
    return infor['car_brands']

@app.get("/brandname/{name}")
def details(name : str = Path(...,description="Hyundai Belongs to South Korea",example="Hyundai")):
  data = load_data()


  brands = data['car_brands']  #here brands has become a list of dictionaries.

  for i in brands:
      if i['brand'] == name:
          return i
      
      raise HTTPException(status_code=404,detail="Not found.")
  