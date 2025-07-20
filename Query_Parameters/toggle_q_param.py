from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/toggle")
def toggle_items(include_archived: bool = Query(False, description="Include archived items", example=True)):
    if include_archived:
        return {"message": "Showing all items, including archived ones."}
    else:
        return {"message": "Showing only active items."}
