from fastapi import FastAPI,Depends,HTTPException

app = FastAPI()

class Auth:
    def __init__(self, token: str = ""):
        self.token = token

    def validate(self):
        if self.token != "admin":
            raise HTTPException(status_code=403, detail="Forbidden")

@app.get("/admin")
def admin_area(auth: Auth = Depends()):
    auth.validate()
    return {"message": "Welcome admin"}
