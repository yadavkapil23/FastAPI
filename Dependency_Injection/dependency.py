from fastapi import FastAPI,Depends

def get_token():
    return "abc123"

app = FastAPI()

@app.get("/items")
def read_items(token: str = Depends(get_token)):
    return {"token_received": token}