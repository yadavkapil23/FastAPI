from fastapi import FastAPI,Depends

app = FastAPI()

#defines a function , that takes a price and returns 90% of its value(10% discount.)
def calculate_discount(price: int):
    return price * 0.9


#creates a GET Endpoint , endpoint expects a query param , price.
#The final_price param uses Depend to call 'calculated_discount' with the given price.
@app.get("/discounted")
def get_discounted_price(price: int, final_price: float = Depends(calculate_discount)):
    return {"discounted_price": final_price}

#it returs the discounted price as a JSON Response.
