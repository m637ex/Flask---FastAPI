# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.


import uvicorn
from fastapi import FastAPI, Request, HTTPException
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates # Динамический HTML через шаблонизатор Jinja
from fastapi.responses import HTMLResponse # Форматирование ответов API
from fastapi.responses import JSONResponse # возвращается ответ JSON с настраиваемым сообщением и кодом состояния.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# app = FastAPI()
app = FastAPI(openapi_url="/api/v1/openapi.json") # Для кастомной документации - openapi_url="/api/v1/openapi.json"
templates = Jinja2Templates(directory="./sem_05/templates")

tasks = []

class Task(BaseModel): # Валидация данных, инача вернет ошибку 422 с описанием ошибки.
    id: int
    title: str # обязательные данные
    description: Optional[str] = None # НЕобязательные данные
    status: Optional[str] = None
    
# для базового заполнения:
task1 = Task(id=1, title='task1', description='task1', status='task1')
task2 = Task(id=2, title='task2', description='task2', status='task2')
tasks = [task1, task2]
    
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
    tasks.append(task) # Добавляем задачу
    logger.info("Task created")
    return task


# Обновляет задачу с указанным идентификатором
@app.put('/tasks/{task_id}') 
async def update_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
            logger.info(f"PUT complate. {task_id = }, {task = }")
            return task 
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete('/tasks/{task_id}') # Удаляет задачу с указанным идентификатором
async def delete_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            logger.info(f"DELITE complate. {task_id = }")
            return {"item_id": tasks.pop(i)} 
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    tasks = []
    uvicorn.run("task_01:app", port=8000)
    
# запуск из консолои uvicorn sem_05.task_01:app --reload

# отправка curl запросов:  Remove-item alias:curl
# curl -X 'POST' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"title\": \"Task1\", \"description\": \"Description1\", \"status\": false}'
# curl -X 'POST' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"title\": \"Task2\", \"description\": \"Description2\", \"status\": false}'
# curl -X 'POST' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"title\": \"Task3\", \"description\": \"Description3\", \"status\": false}'

