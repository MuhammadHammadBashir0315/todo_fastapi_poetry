from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from todo_poetry.main import app
from sqlmodel import Session , create_engine, SQLModel
from todo_poetry.settings import get_session

# URL = "postgresql://hammad.bashir0315:JPtH6Ecbpk0x@ep-tiny-bar-64942038.us-east-2.aws.neon.tech/todotest?sslmode=require"
engine = create_engine(
    "postgresql://hammad.bashir0315:JPtH6Ecbpk0x@ep-tiny-bar-64942038.us-east-2.aws.neon.tech/todotest?sslmode=require", echo=True
)
def override_get_session():
    with Session(engine) as session:
        yield session
app.dependency_overrides[get_session] = override_get_session
SQLModel.metadata.create_all(engine)
client = TestClient(app)


def test_create_a_task():
    task_data = {"id":1 , "title":"get the clothes" , "description":"go to the mall and get the clothes"}
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_data["id"]
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    return data["id"]
def test_get_tasks():
    task_id = test_create_a_task()
    response = client.get("/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == data.title
    assert data["description"] == data.description