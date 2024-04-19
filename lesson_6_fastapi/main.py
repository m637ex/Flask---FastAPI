import uvicorn
from typing import List
from fastapi import FastAPI
# Модель данных — это класс Python, определяющий поля и их типы для описания
# данных. Для определения моделей данных в FastAPI используется класс BaseModel из модуля pydantic.
from pydantic import BaseModel
# Функция Field позволяет задавать различные параметры для поля, такие как тип
# данных, значение по умолчанию, ограничения на значения и т.д.
from pydantic import Field
# Перечень принимаемых функцией Field параметров
# Для валидации данных можно использовать следующие параметры при создании моделей:
# ● default: значение по умолчанию для поля
# ● alias: альтернативное имя для поля (используется при сериализации и десериализации)
# ● title: заголовок поля для генерации документации API
# ● description: описание поля для генерации документации API
# ● gt: ограничение на значение поля (больше указанного значения)
# ● ge: ограничение на значение поля (больше или равно указанному значению)
# ● lt: ограничение на значение поля (меньше указанного значения)
# ● le: ограничение на значение поля (меньше или равно указанному значению)
# ● multiple_of: ограничение на значение поля (должно быть кратно указанному значению)
# ● max_length: ограничение на максимальную длину значения поля
# ● min_length: ограничение на минимальную длину значения поля
# ● regex: регулярное выражение, которому должно соответствовать значение поля



app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title="Name", max_length=50) # максимальная длина 10 символов ...,-обязательное поле
    price: float = Field(..., title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10)
    is_offer: bool = None
    
    
class User(BaseModel):
    username: str
    full_name: str = None
    age: int = Field(default=0) # значение по умолчанию
    
    
class Order(BaseModel):
    items: List[Item] # модель списка Item
    user: User # модель пользователя
    
    
@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)