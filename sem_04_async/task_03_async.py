# Асинхронная загрузка с использованием модуля asyncio:
# Здесь мы используем модуль asyncio для асинхронной загрузки страниц. Мы
# создаем функцию download, которая использует aiohttp для получения
# html-страницы и сохранения ее в файл. Затем мы создаем асинхронную функцию
# main, которая запускает функцию download для каждого сайта из списка urls и
# ожидает их завершения с помощью метода gather. Мы запускаем функцию main с
# помощью цикла событий asyncio.

import asyncio
import aiohttp # pip install aiohttp - асинхронный модуль для получения из сети данных(типа reguest но асинхронный) 
import time
from os import chdir
chdir(fr'G:\YandexDisk\GB\Python\Flask и FastAPI\sem_04_async\sites')

urls = [    
    'https://www.google.ru/',
    'https://gb.ru/',
    'https://www.python.org/',
    'https://www.youtube.com/',
    'https://www.pinterest.com/',
    'https://www.tumblr.com/',
    'https://similarweb.com/',
    'https://dtf.ru/',
    'https://pikabu.ru/',
    'https://tinkoff.ru/',
]

async def download(url):
    async with aiohttp.ClientSession() as session: # создаём сессию с клиентом как объект session
        async with session.get(url) as response: # асинхронно оплучаем инф-у по указанному адресу
            text = await response.text() # получаем текст сообщения
            filename = 'asyncio_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

async def main():
    tasks = [] # пустой списко задач
    for url in urls: # перебираем нашт адреса
        task = asyncio.ensure_future(download(url)) # создаём задачу и 
        tasks.append(task) # добавляем её в список задач
    await asyncio.gather(*tasks) # выполни все 5 задач одновременно асинхронно
    
start_time = time.time() # запоминаем начало работы программы

if __name__ == '__main__':
    loop = asyncio.get_event_loop() # в переменную loop получаем цикл событий
    loop.run_until_complete(main()) # цикл событий, запусти корутину main до тех пор пока она не завершится.
    