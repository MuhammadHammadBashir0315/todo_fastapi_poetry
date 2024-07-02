from fastapi import APIRouter

from todo_poetry.public.task import views as task

api = APIRouter()
api.include_router(task.router, prefix="/tasks")