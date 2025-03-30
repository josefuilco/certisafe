from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

class Enviroment(BaseModel):
    ORIGIN_CLIENT: str = Field(min_length=1)
    POSTGRES_HOST: str = Field(min_length=1)
    POSTGRES_PORT: int = Field(default=5432)
    POSTGRES_USER: str = Field(min_length=1)
    POSTGRES_PASSWORD: str = Field(min_length=1)
    POSTGRES_DB: str = Field(min_length=1)

env = Enviroment(
    ORIGIN_CLIENT=os.getenv("ORIGIN_CLIENT"),
    POSTGRES_HOST=os.getenv("POSTGRES_HOST"),
    POSTGRES_PORT=int(os.getenv("POSTGRES_PORT")),
    POSTGRES_USER=os.getenv("POSTGRES_USER"),
    POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD"),
    POSTGRES_DB=os.getenv("POSTGRES_DB")
)