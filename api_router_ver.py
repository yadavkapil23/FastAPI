from fastapi import FastAPI,APIRouter

#from v1_router import v1_router

my_router = APIRouter(
    prefix="/kapil",
    responses={
        404 : {'description' : 'details not found.'}
    }
)

app = FastAPI()

app.include_router(my_router)

#app.include(router) - >it will include the v1 router.