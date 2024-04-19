from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

tasks = {}

# Создаем модель данных
class Task(BaseModel):
    title: str
    description: str
    completed: Optional[bool] = True # По умолчанию задача выполнена

# GET запросы используются для получения данных с сервера.
@app.get("/") 
async def root():
    return {"Hello": "World"}


# Возвращает список всех задач
@app.get('/tasks/') 
async def read_tasks():
    return tasks


# Возвращает задачу с указанным идентификатором
@app.get('/tasks/{task_id}') 
async def read_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


# Добавляет новую задачу
@app.post('/tasks/') 
async def create_task(task: Task):
    task_id = max(tasks.keys(), default=0) + 1 # Создаем уникальный идентификатор задачи
    tasks[task_id] = task # Добавляем задачу
    return task


# Обновляет задачу с указанным идентификатором
@app.put('/tasks/{task_id}') 
async def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task # Обновляем задачу
    return task


@app.delete('/tasks/{task_id}') # Удаляет задачу с указанным идентификатором
async def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks[task_id]
    task.completed = False # Помечаем задачу как не выполненную
    tasks[task_id] = task # Обновляем задачу
    return {"detail": "Task deleted"}



# Запуск сервера: uvicorn sem_05.hw1_main:app --reload

# отправка curl запросов:  Remove-item alias:curl
# curl -X 'POST' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"title\": \"Task1\", \"description\": \"Description1\", \"completed\": false}'
# curl -X 'POST' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"title\": \"Task2\", \"description\": \"Description2\", \"completed\": false}'
# curl -X 'POST' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"title\": \"Task3\", \"description\": \"Description3\", \"completed\": false}'

# результат: http://127.0.0.1:8000/tasks/

