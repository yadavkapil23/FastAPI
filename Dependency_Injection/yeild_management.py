from fastapi import FastAPI,Depends

def get_resource():
    resource = "🗃️ Opened resource"
    print(resource)
    try:
        yield resource
    finally:
        print("Closed resource")

@app.get("/use")
def use_resource(r = Depends(get_resource)):
    return {"resource": r}
