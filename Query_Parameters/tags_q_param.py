from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get("/tags")
def get_by_tags(tags: List[str] = Query(..., description="Tags to filter by", example=["ai", "ml"])):
    return {"Selected Tags": tags}
