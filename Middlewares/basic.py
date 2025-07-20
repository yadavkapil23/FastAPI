from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")  #tells fastapi to use the function below as middleware for every HTTP request.
async def log_time(request: Request, call_next): #this function will run for every req your app receives.
    
    
    start = time.time() #records current time before handling the request.

    response = await call_next(request)  #passes req toa actual endpoint. , and waits for response.
    duration = time.time() - start #calc how long it took to handle req.
    print(f"{request.method} {request.url.path} took {duration:.3f}s") #print out HTTP method


    #returns response back to user.
    return response
