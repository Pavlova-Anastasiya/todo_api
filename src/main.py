from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


@app.get("/")
def read_root():
    return {"message": "Hello, Todo API!"}


todos = []

@app.post("/tasks")
def create_task(todo: Todo):
  todos.append(todo)
  return {"message": "Задача успешно создана!", "task": todo}

@app.get('/tasks')
def get_task():
    return {'task': todos}

@app.get('/tasks/{task_id}')
def task_id(task_id: int):
    for t in todos:
        if t.id == task_id:
            return t
    else:
        return None


@app.delete('/tasks/{task_id}')
def delete_id(task_id: int):
    for t in todos:
        if t.id == task_id:
            todos.remove(t)
            return {"message": "Задача успешно удалена!", "task": t}
    return {"message": "Задача с таким ID не найдена"}


@app.put('/tasks/{task_id}')
def update_task(task_id: int, updated_task: Todo):
    for index, t in enumerate(todos):
        if t.id == task_id:
            todos[index] = updated_task
            return {"message": "Задача успешно обновлена!", "task": updated_task}
    return {"message": "Задача с таким ID не найдена"}