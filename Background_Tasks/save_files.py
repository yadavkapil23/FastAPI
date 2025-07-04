from fastapi import FastAPI,BackgroundTasks

app = FastAPI()

def save_to_file(data: str):
    with open("logs.txt", "a") as file:
        file.write(data + "\n")

@app.post("/log")
def log_message(msg: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(save_to_file, msg)
    return {"message": "Logging in background"}
