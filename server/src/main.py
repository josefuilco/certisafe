from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.configuration import env
from src.routes import (
    auth_router,
    condition_router,
    faculty_router,
)

# FastApi app instance
app = FastAPI(
    title='CertiSafe API',
    description='API para la gestión segura de eventos y sus certificados',
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[env.ORIGIN_CLIENT],
    allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
    allow_headers=['Authorization', 'Content-Type'],
    expose_headers=['x-api-token']
)

# Includes routes
app.include_router(auth_router)
app.include_router(condition_router)
app.include_router(faculty_router)
