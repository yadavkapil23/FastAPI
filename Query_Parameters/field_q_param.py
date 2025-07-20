#field query params are used to specify which fields to get in response.
from fastapi import FastAPI,Path,Query,HTTPException

app = FastAPI()

@app.get("/details/{info}")
def information(
    info : str = Path(...,description="Comma separated fields",example="name,email"),
    fields :str = Query(...)
                ):
    data = {
        "id": 1,
        "name": "Kapil",
        "email": "kapil@example.com",
        "location": "India",
        "status": "active"
    }

    result = []
    
    selected_fields = fields.split(",")

    for i in selected_fields : 
        if fields in data:
            result[fields] = data[fields]
            return result
        
    raise HTTPException(status_code=404,detail="Not Found.")

