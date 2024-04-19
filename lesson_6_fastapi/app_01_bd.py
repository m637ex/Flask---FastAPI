# venv - .\.venv\Scripts\Activate.ps1
# pip install sqlalchemy
# pip install databases[aiosqlite]

import uvicorn
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field # испльзуем в моделях
from typing import List
from fastapi import Path # используем в пути
from fastapi import Query # используем в пара ключ:значение
# На самом деле Query, Path, Field и другие фильтры создают объекты подклассов общего класса Param,

# /docs
# /redoc

DATABASE_URL = "sqlite:///lesson_6_fastapi/mydatabase.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname" # PostgreSQL

database = databases.Database(DATABASE_URL) 
metadata = sqlalchemy.MetaData() # используем декларативный метод работы с базой данных

# В FastAPI с SQLAlchemy ORM мы можем создавать эти операции, используя функции и методы Python.
# ● CREATE, Создать: добавление новых записей в базу данных.
# ● READ, Чтение: получение записей из базы данных.
# ● UPDATE, Обновление: изменение существующих записей в базе данных.
# ● DELETE, Удалить: удаление записей из базы данных.

# создаём таблицу для БД
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    )

# формируем таблицы в БД:
engine = sqlalchemy.create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} # только для sql баз данных
    ) 
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup") # запуск нашего приложения
async def startup():
    await database.connect()

@app.on_event("shutdown") # остановка нашего приложения
async def shutdown():
    await database.disconnect()
    

# Модели данных
class UserIn(BaseModel): # Использeем при добавлении данных id присвоится автоматически т.к. в БД указано primary_key=True
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)
    
    
class User(BaseModel): # используем при чтении/изменении
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# @app.get("/fake_users/{count}") # добавим фейковых пользователей # комментирыем от греха подальше
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
#         await database.execute(query) # асинхронный запрос на добавление
#     return {'message': f'{count} fake users create'}


# !!!!!!!!!!!Формирование CRUD!!!!!!!!!!!!
@app.post("/users/", response_model=User) # ➢Создание пользователя в БД, create
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email) # .insert() - вставка новых данных
    query = users.insert().values(**user.dict()) # аналогично строчке выше
    last_record_id = await database.execute(query) # отправляем данные в БД
    return {**user.dict(), "id": last_record_id}

@app.get("/users/", response_model=List[User]) # ➢Чтение пользователей из БД, read
async def read_users(): # формируем запрос
    query = users.select() # выбери всех
    return await database.fetch_all(query) #  верни всех в виде списка

@app.get("/users/{user_id}", response_model=User) # ➢Чтение одного пользователя из БД, read
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id) # users.c.id - таблица users, c.id - колонка id
    return await database.fetch_one(query) #  верни одного пользователя

@app.put("/users/{user_id}", response_model=User) # ➢Обновление пользователя в БД, update
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict()) # .values(**new_user.dict()) преарати из модели pandentic в словарь, распокуй и обнови данные у найденного пользователя
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}

@app.delete("/users/{user_id}") # ➢Удаление пользователя из БД, delete
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}

# Проверка параметра пути через Path:
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item", ge=1), q: str = None):
    return {"item_id": item_id, "q": q}


# Проверка параметра запроса через Query:
@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3,max_length=50)): # None - необязательный параметр
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results



if __name__ == "__main__":
    uvicorn.run("app_01_bd:app", port=8000)
    
# запуск из консолои uvicorn lesson_6_fastapi.app_01_bd:app --reload

# curl -X 'POST' \
# 'http://127.0.0.1:8000/users/' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
# "name": "Alex",
# "email": "my@mail.ru"
# }'