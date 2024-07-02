from fastapi import FastAPI,  APIRouter , Depends, Query

from todo_poetry.public.task.crud import create_task, delete_task, read_task, read_tasks, update_task
from todo_poetry.public.task.models import TaskRead, TaskCreate, TaskUpdate
from sqlmodel import Session
from todo_poetry.settings import get_session

router = APIRouter()
@router.post("/create", response_model=TaskRead)
def create_a_task(task: TaskCreate, db: Session = Depends(get_session)):
    
    return create_task(task=task, db=db)

@router.get("", response_model=list[TaskRead])
def get_tasks(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    return read_tasks(offset=offset, limit=limit, db=db)

# need authentication at this endpoint
@router.get("/{task_id}", response_model=TaskRead)
def get_a_task(task_id: int, db: Session = Depends(get_session)):
    return read_task(task_id=task_id, db=db)

#need authentication at this point
@router.patch("/{task_id}", response_model=TaskRead)
def update_a_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_session)):
    return update_task(task_id=task_id, task=task, db=db)

#need this authentication at this point
@router.delete("/{task_id}")
def delete_a_task(task_id: int, db: Session = Depends(get_session)):
    return delete_task(task_id=task_id, db=db)