from fastapi import FastAPI,HTTPException,Path,Query
import json

app = FastAPI()

def load_data():
    with open('presidents.json','r') as f:
        data = json.load(f)
        return data

@app.get("/")
def home():
    return "Welcome to our Home."

@app.get("/info")
def info():
    data = load_data()
    return data['countries']

@app.get("/leader/{president}")
def president_info(president : str = Path(...,description="President of US is Donald Trump",example="Donald Trump")):
    data = load_data()
    supreme = data['countries']

    for i in supreme:
        if i['president']['name'].lower() == president.lower():
         return{
             "country" : i['name'],
        "president" : i['president']
         }
    raise HTTPException(status_code=404, detail="NO PRESIDENT.")


@app.get("/nation/{country}")
def get_country(country : str = Path(...,description="Country is United States",example="United States of America.")):
    data = load_data()

    country_data = data['countries']

    for i in country_data:
        if i['name'].lower() == country.lower():
            return{
                "country" : i['name'],
                "party" : i['president']['political_party']  #Go into president → get political party
            }
    raise HTTPException(status_code=404,detail="ERROR")

#now using the Query param.
@app.get("/greet/{name}")
def greeting(name : str = Path(...,description="Good Morning Joe Biden",example="Joe Biden"),
             detail : bool = Query(False,description="If true , show detailed info.")):
     if detail:
        return {
            "message": f"Good morning, {name}!",
            "note": "Hope you have a wonderful and productive day!"
        }
     else:
        return {
            "message": f"Good morning, {name}!"
        }