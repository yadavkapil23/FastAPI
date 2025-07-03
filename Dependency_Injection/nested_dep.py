from fastapi import FastAPI,HTTPException,status,Depends

app = FastAPI()

def get_db():
    return {"users": ["Alice", "Bob"]}

def get_user(db = Depends(get_db)):
    return db["users"][0]

@app.get("/me")
def read_current_user(user: str = Depends(get_user)):
    return {"current_user": user}
