
from sqlmodel import Session, select
from fastapi import Depends, HTTPException, status
from todo_poetry.public.task.models import Task, TaskCreate, TaskUpdate
from todo_poetry.settings import get_session

def create_task(task: TaskCreate , db: Session = Depends(get_session)):
    task_to_db = Task.model_validate(task)
    db.add(task_to_db)
    db.commit()
    db.refresh(task_to_db)
    return task_to_db

def read_tasks(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    tasks = db.exec(select(Task).offset(offset).limit(limit)).all()
    return tasks

def read_task(task_id: int, db: Session = Depends(get_session)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student not found with id: {task_id}",
        )
    return task

def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_session)):
    task_to_update = db.get(Task, task_id)
    if not task_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student not found with id: {task_id}",
        )

    task_data = task.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task_to_update, key, value)

    db.add(task_to_update)
    db.commit()
    db.refresh(task_to_update)
    return task_to_update

def delete_task(task_id: int, db: Session = Depends(get_session)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student not found with id: {task_id}",
        )

    db.delete(task)
    db.commit()
    return {"ok": True}

