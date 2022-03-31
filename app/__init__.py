from fastapi import FastAPI
from app.api.router import route

app = FastAPI(
    title='Belajar API2',
    version='1.0.0',
)

app.include_router(route)