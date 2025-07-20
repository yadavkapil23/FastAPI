from fastapi import FastAPI,Query,HTTPException

app = FastAPI()

@app.get("/greet")
def greeting(name : str = Query("Guest",description="Good Evening Guest")):
    return f"Hello {name}"

# http://127.0.0.1:8000/greet?name=Kapil