from typing import Optional, Annotated, Union
from sqlmodel import SQLModel , Field

class TaskBase(SQLModel):
    title : str
    description : Optional[str] = Field(nullable=True)
    class Config:
        json_schema_extra = {
            "example":{
            "id":1,
            "title":"get the clothes",
            "description":"go and get the clothes from the mall "
            }
        }
        
class Task(TaskBase , table=True):
    id: Optional[int] = Field(default=None , primary_key=True)

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id : int
    title : str
    description : str

class TaskUpdate(TaskBase):
    title :str
    description : Optional[str] = Field(nullable=True)
    
    class Config:
        json_schema_extra = {
            "example":{
                "title":"get the clothes",
                "description": "go and get the clothes from the mall"
            }
        }
