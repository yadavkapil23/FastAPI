from fastapi import FastAPI,HTTPException,Path
import json

app = FastAPI()

def load_data():
    with open('brand.json','r') as f:
     data = json.load(f)
    return data['car_brands']


@app.get("/")
def home():
    return {'message':'Welcome to Home.'}

@app.get("/info")
def info():
    info = load_data()
    return info

@app.get("/nationality/{country}")
def details(country : str = Path(...,description="Tesla belongs to USA",example="USA")):
   
   information = load_data() #loads the car brand data from our file.

   matching_list = [] #initialising the list to store the matching brands

   for brand in information: #looping over each brand in json
      
      if brand['country'] == country: #checks whether the brand's country matches the path parameter.
         matching_list.append(brand) #if matches , it appends in that list.

   #if matching_list: #checks if list is not empty.
      return matching_list #returns the list.
   
   raise HTTPException(status_code=404,detail="Not found.")#if no matches found , raise exception