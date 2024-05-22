from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(Task):
    pass

class TaskUpdate(Task):
    pass

class Task(Task):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True