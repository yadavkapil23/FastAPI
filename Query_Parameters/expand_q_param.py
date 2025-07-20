from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/expand")
def expand_fields(expand: str = Query(..., description="Fields to expand", example="profile,settings")):
    expanded = expand.split(",")
    return {"Expanded Sections": expanded}
