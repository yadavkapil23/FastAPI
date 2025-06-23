from fastapi import FastAPI,Query

app = FastAPI()
@app.get("/filter")
def filtered(value : str = Query(...,description="This is filtered value.",example="FILTERED")):
    return {
        "Your filtered value " : value
    }