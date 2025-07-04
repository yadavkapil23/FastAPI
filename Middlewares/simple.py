from fastapi import FastAPI,middleware,Request
import time

app = FastAPI()

@app.middleware('http')
async def middleware( request : Request , call_next):
    start = time.time()
    print("before functional.")
    response = await call_next(request)
    print("after functional.")
    end = time.time() - start
    response.headers['X-process-time'] = str(end)
    return response


@app.get("/")
async def home():
    print("Function Call")
    return{
        "name" : "Seong Gi Hun",
        "city" : "Seoul , South Korea"
    }