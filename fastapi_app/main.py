from fastapi import FastAPI
from routers import users #it imports the users router from routers package.
# This imports the 'users' module from the 'routers' package.
# The 'users' module contains the code for user-related API endpoints.

app = FastAPI()

# Register the controller
app.include_router(users.router)
# This line adds the user-related routes (endpoints) from the 'users' router to your FastAPI app.
# All endpoints defined in 'users.router' become part of your API.


#ENTRY POINT OF OUR FASTAPI APP.