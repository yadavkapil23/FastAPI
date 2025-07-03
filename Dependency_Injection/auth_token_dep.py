from fastapi import HTTPException, status,Depends,FastAPI

app = FastAPI()

def get_token(token: str = ""):
    if token != "securetoken":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    return token

@app.get("/protected")
def protected_route(token: str = Depends(get_token)):
    return {"message": "Access granted"}
