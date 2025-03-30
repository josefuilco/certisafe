from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.configuration import env

# FastApi app instance
app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[env.ORIGIN_CLIENT],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['Authorization', 'Content-Type'],
)

@app.get('/')
async def root():
    return {'message': 'Hello World!'}