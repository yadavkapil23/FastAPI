from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/search")
def search_item(q : str = Query(...,description="Search Keyword",example="laptop")):
    return {
        "You Searched for" : q
    }