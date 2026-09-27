from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

todos = []

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    for t in todos:
        if t.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo already exists")
    todos.append(todo)
    return todo

@app.get("/todos/")
def list_todos():
    return todos

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            del todos[i]
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
