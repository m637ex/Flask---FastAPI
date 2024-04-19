# Задание
# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.
# Критерии оценивания:
# - Слушатель создал базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.

# python -m venv .venv
# .\.venv\Scripts\Activate.ps1
# pip install faker
# pip install sqlalchemy
# pip install fastapi
# pip install uvicorn
# pip install databases

import uvicorn
from typing import List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
import databases
import sqlalchemy
import aiosqlite
import datetime
from random import randint
from faker import Faker # Faker - это библиотека для генерации случайных данных на различных языках программирования
fake = Faker()

# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.

DATABASE_URL = "sqlite:///sem_06_fastapi/mydatabase.db"

database = databases.Database(DATABASE_URL) 
metadata = sqlalchemy.MetaData() # используем декларативный метод работы с базой данных

# В FastAPI с SQLAlchemy ORM мы можем создавать эти операции, используя функции и методы Python.
# ● CREATE, Создать: добавление новых записей в базу данных.
# ● READ, Чтение: получение записей из базы данных.
# ● UPDATE, Обновление: изменение существующих записей в базе данных.
# ● DELETE, Удалить: удаление записей из базы данных.

# создаём таблицу для БД
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("product_name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(256)),
    sqlalchemy.Column("price", sqlalchemy.Float),
    ) # создание таблицы products в базе данных с полями id, product_name, description, price и типами данных

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(32)),
    sqlalchemy.Column("lastname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    ) # создание таблицы users в базе данных с полями id, firstname, lastname, email, password и типами данных

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('product_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column('order_date', sqlalchemy.DateTime, default=datetime.datetime.now()),
    sqlalchemy.Column('status', sqlalchemy.String(64), default='new')
) # создание таблицы orders в базе данных с полями id, user_id, product_id, order_date, status и типами данных

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False}) # создание объекта Engine
metadata.create_all(engine) # создание таблицы в базе данных

app = FastAPI()

# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.

class UserIn(BaseModel):
    firstname: str = Field(max_lenght=32)
    lastname: str = Field(max_lenght=32)
    email: str = Field(max_lenght=128)
    password: str = Field(max_lenght=128)

class User(BaseModel):
    id: int
    firstname: str = Field(max_lenght=32)
    lastname: str = Field(max_lenght=32)
    email: str = Field(max_lenght=128)
    password: str = Field(max_lenght=128)
    
class ProductIn(BaseModel):
    product_name: str = Field(max_lenght=32)
    description: str = Field(max_lenght=256)
    price: float = Field(gt=0)

class Product(BaseModel):
    id: int
    product_name: str = Field(max_lenght=32)
    description: str = Field(max_lenght=256)
    price: float = Field(gt=0)

class OrderIn(BaseModel):
    user_id: int
    product_id: int
    order_date: str = Field(max_lenght=64)
    status: str = Field(max_lenght=64)

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: datetime.datetime
    status: str = Field(max_lenght=64)
    
# заполнение таблиц фейковыми данными
@app.get('/create_fake/{count_users}/{count_products}/{count_orders}')
async def create_user(count_users: int, count_products: int, count_orders: int):
    for i in range(count_users):
        query = users.insert().values(
            firstname=fake.first_name(), 
            lastname=fake.last_name(), 
            email=fake.ascii_company_email(), 
            password=fake.swift(length=11))
        await database.execute(query)
    for i in range(count_products):
        query = products.insert().values(
            product_name=fake.word(), 
            description=fake.text(max_nb_chars=256), 
            price=randint(1, 100_000))
        await database.execute(query)
    for i in range(count_orders):
        query = orders.insert().values(
            user_id=randint(1, count_users),
            product_id=randint(1, count_products), 
            order_date=fake.date_time_this_month(), 
            status=fake.word(ext_word_list=['new', 'old', 'delete', 'wait']))
        await database.execute(query)        
    return {'message': f'Create fake {count_users} users, {count_products} protucts and {count_orders} orders'}


# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

# CREATE - создание записи
@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, surname=user.surname, email=user.email, password=user.password)
    last_record_id = await database.execute(query) # ожидание выполнения запроса к базе данных
    return {**user.dict(), 'id': last_record_id}

# READ - чтение записи
@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

# CREATE - создание записи
@app.post('/products/', response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(product_name=product.product_name, description=product.description, price=product.price)
    last_record_id = await database.execute(query)
    return {**product.dict(), 'id': last_record_id}

# READ - чтение записи
@app.get('/products/', response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)

# CREATE - создание записи
@app.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, product_id=order.product_id, order_date=datetime.datetime.now(), status=order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), 'id': last_record_id}

# READ - чтение записи
@app.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


# UPDATE - изменение записи
@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, user: UserIn):
    query = users.update().where(users.c.id == user_id).values(name=user.name, surname=user.surname, email=user.email, password=user.password)
    await database.execute(query)
    return {**user.dict(), 'id': user_id}

# UPDATE - изменение записи
@app.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(product_name=product.product_name, description=product.description, price=product.price)
    await database.execute(query)
    return {**product.dict(), 'id': product_id}

# UPDATE - изменение записи
@app.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(user_id=order.user_id, product_id=order.product_id, order_date=datetime.datetime.now(), status=order.status)
    await database.execute(query)
    return {**order.dict(), 'id': order_id}

# DELETE - удаение записи
@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'user with id {user_id} deleted'}

# DELETE - удаение записи
@app.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': f'product with id {product_id} deleted'}

# DELETE - удаение записи
@app.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': f'order with id {order_id} deleted'}


@app.on_event("startup") # событие startup, которое происходит при запуске приложения
async def startup():
    await database.connect() # подключение к базе данных

@app.on_event("shutdown")  # app.on_event - это декоратор, события
async def shutdown():
    await database.disconnect() # отключение от базы данных

if __name__ == '__main__':
    uvicorn.run('hw1_main:app', host='127.0.0.1', port=8000)