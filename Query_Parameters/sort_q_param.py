from fastapi import FastAPI,Query,Path

app = FastAPI()

@app.get("/sort/{sort_order}")
def sorting(sort_order : str = Path(...,description="Sorting orders : Asc, Desc",example="Asc"),
            order : str = Query("asc",description="Choose Sort order : asc or desc.",example="asc")):
    return {
        "Order Choosen": order,
        "Path Order Chosen" : sort_order
    }