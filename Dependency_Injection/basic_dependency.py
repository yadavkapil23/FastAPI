from fastapi import FastAPI,Depends

app = FastAPI()

def greet():
    return " Hello , Good Morning Buddy!"

@app.get("/home")
def home(message : str = Depends(greet)):
    return{
        "message" : message
    }