from fastapi import FastAPI,Path,Query

app = FastAPI()

@app.get("/home/{item_name}")
def item_nos(
    item_name : str = Path(...,description="Showing 10 results per page.",example="10 results , 20 results"),
    no_of_items : int = Query(10,description="Show 10 results",example=10)
             ):
    return{
        "Name of Item" : item_name,
        "No of Items" : no_of_items
    }
    