from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import Task, TaskCreate, User, UserCreate
from crud import create_task, get_tasks, get_task, get_users, delete_task, create_user, delete_user
from database import get_db
import models, schemas


app = FastAPI()

@app.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    print("create_new_user was called")
    return create_user(db=db, user=user)

@app.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    print("read_users was called")
    users = get_users(db, skip=skip, limit=limit)
    return users

@app.post("/tasks/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)): 
    print("create_task was called")
    return create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    print("read_tasks was called")
    tasks = get_tasks(db, skip=skip, limit=limit)
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    print("read_task was called")
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        print("Task not found")
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        return None
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task_by_id(task_id: int, db: Session = Depends(get_db)):  
    print("delete_task_endpoint was called")
    return delete_task(db=db, task_id=task_id)

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_users(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user