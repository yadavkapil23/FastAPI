from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def home(request : Request):
    return templates.TemplateResponse("index.html",{"request":request,"username":"Kapil"})

@app.get("/skills",response_class=HTMLResponse)
async def skillset(request : Request):
    return templates.TemplateResponse("profile.html",{"request":request,"username":"Kapil","skill" : ["Java","Python","C++"]})