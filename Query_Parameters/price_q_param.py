from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/price")
def filter_by_price(min_price: int = Query(0, description="Minimum price filter", example=500)):
    return {
        "message": f"Showing products priced above ₹{min_price}"
    }
