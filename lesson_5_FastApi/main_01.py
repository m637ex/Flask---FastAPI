# FASTAPI
# venv - python -m venv .venv
# venv - .\.venv\Scripts\Activate.ps1
# Установка pip install fastapi
# асинхронный сервер ASGI сервер - pip install "uvicorn[standard]"
# запуск сервера приложений форма - uvicorn main:app --reload 
# запуск сервера приложений - uvicorn lesson_5_FastApi.main_01:app --reload

# Для curl запросов: Remove-item alias:curl

# Для просмотра интерактивной документации Swagger нужно запустить приложение
# и перейти по адресу http://localhost:8000/docs
# Альтернативная документация http://localhost:8000/redoc

from fastapi import FastAPI, Request, HTTPException
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse # Форматирование ответов API
from fastapi.responses import JSONResponse # возвращается ответ JSON с настраиваемым сообщением и кодом состояния.
from fastapi.templating import Jinja2Templates # Динамический HTML через шаблонизатор Jinja
from fastapi.openapi.utils import get_openapi # Для генерации документации нужно создать экземпляр класса FastAPI с параметром openapi_url:



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# app = FastAPI()
app = FastAPI(openapi_url="/api/v1/openapi.json") # Для кастомной документации - openapi_url="/api/v1/openapi.json"
templates = Jinja2Templates(directory="./lesson_5_FastApi/templates")


class Item(BaseModel): # Если данные не соответствуют описанию класса Item, то FastAPI вернет ошибку 422 с описанием ошибки.
    name: str # обязательные данные
    description: Optional[str] = None # НЕобязательные данные
    price: float # обязательные данные
    tax: Optional[float] = None # НЕобязательные данные

# !!!!!!!!!!!!!Обработка HTTP-запросов и ответов!!!!!!!!!!
# GET - получить данные с сервера
# POST - отправить на сервер
# PUT - обновить на сервере
# DELETE - удалить на сервере (в бд)

# @app.get("/") # главная страница
# async def root():
#     logger.info('Отработал GET запрос.')
#     return {"message": "Hello World"}

@app.get("/", response_class=HTMLResponse) # генерация страницы HTML
async def read_root():
    return "<h1>Hello World</h1>"

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q: # если есть параметр q
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)


@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
# обработка данных
    return {"user_id": user_id, "order_id": order_id}

@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("item.html", {"request": request, "name": name})


@app.get("/items/") # http://127.0.0.1:8000/items/?limit=25
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}


# генерация автоматической документации
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My Custom title",
        version="1.0.1",
        description="This is a very custom OpenAPI schema", 
        routes=app.routes,
        )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi



# Remove-item alias:curl

# POST запрос:
# curl -X 'POST' 'http://127.0.0.1:8000/items/' 
# -H 'accept: application/json' 
# -H 'Content-Type: application/json' 
# -d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'

# то же в одну строку
# curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'
# Через PS: curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"name\": \"BestSale\", \"description\": \"The best of the best\", \"price\": 9.99, \"tax\": 0.99}'

# PUT запрос:
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' 
# -H 'accept:application/json' 
# -H 'Content-Type: application/json' 
# -d '{"name": "NewName", "description": "New description of the object", "price": 77.7, "tax": 10.01}'

# то же в одну строку
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:application/json' -H 'Content-Type: application/json' -d '{\"name\": \"NewName\", \"description\": \"New description of the object\", \"price\": 77.7, \"tax\": 10.01}'


# Хороший короткий PUT запрос:
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"name\": \"NewName\", \"price\": 77.7}'
# Плохой PUT запрос:
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"name\": \"NewName\", \"tax\": 77.7}'

# DELETE Запрос:
# curl -X 'DELETE' 'http://127.0.0.1:8000/items/13' -H 'accept: application/json'

