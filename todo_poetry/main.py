from contextlib import asynccontextmanager
from fastapi import FastAPI
from todo_poetry.public import api as public_public
from fastapi import APIRouter
from todo_poetry.settings import create_db_and_tables

app = FastAPI()
api = APIRouter()




app.include_router(public_public)
@asynccontextmanager
async def lifespan(app: FastAPI):
    
    print("Creating tables..")
    create_db_and_tables()
    yield





