# Загрузка в 5 потоков с использованием модуля threading:
#     Здесь мы создаем функцию download, которая загружает html-страницу и сохраняет
# ее в файл. Затем мы создаем по одному потоку для каждого сайта из списка urls,
# передавая функцию download в качестве целевой функции для каждого потока. Мы
# запускаем каждый поток и добавляем его в список threads. В конце мы ждем
# завершения всех потоков с помощью метода join.

import requests
import threading
import time
from os import chdir
chdir(fr'G:\YandexDisk\GB\Python\Flask и FastAPI\lesson_4_mnogozad')

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]

def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")
        
threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url]) # создаём отдельный поток для каждой ссылки
    threads.append(thread) # добавляем поток в список потоков
    thread.start() # Стартуем все потоки
for thread in threads:
    thread.join() # Ждем пока все потоки завершат свою работу

# Downloaded https://www.python.org/ in 0.82 seconds
# Downloaded https://ya.ru/ in 0.87 seconds
# Downloaded https://www.google.ru/ in 0.93 seconds
# Downloaded https://habr.com/ru/all/ in 0.99 seconds
# Downloaded https://gb.ru/ in 1.12 seconds