from fastapi import FastAPI
from routers.studentrouter import srouter

app = FastAPI()

app.include_router(srouter)
