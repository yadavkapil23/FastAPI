from fastapi import FastAPI,Depends

app = FastAPI()

def get_db():
    db = {"users": ["Alice", "Bob"]}
    try:
        yield db  # give the database
    finally:
        pass  # here you would close DB in real app

#defined a dependency function called get_db.
#it creates a fake db , dictionaries with a "users list."
#function yields the db object , making it available to endpoints that depend on it.
#th finally block is where u close a real db connection.


@app.get("/users")
def list_users(db=Depends(get_db)):
    return db["users"]

#defines a get endpoint , the db param uses Depends to get value from get_db.
#returns the list of users from database.