from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

# Background function
def send_email(email: str):
    print(f" Sending email to {email}...")
    # Simulate delay
    import time
    time.sleep(2)
    print("Email sent!")

@app.post("/register/")
def register_user(email: str, background_tasks: BackgroundTasks):
    # Add background task
    background_tasks.add_task(send_email, email)
    return {"message": "User registered. Email will be sent in background."}
