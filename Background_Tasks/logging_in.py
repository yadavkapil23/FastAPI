from fastapi import FastAPI,BackgroundTasks

app = FastAPI()

def log_action(user_id: int, action: str):
    print(f"User {user_id} performed: {action}")

@app.post("/click")
def click_button(user_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(log_action, user_id, "clicked_button")
    return {"message": "Click received"}
