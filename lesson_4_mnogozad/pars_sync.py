# Обычная синхронная загрузка:
# В данном примере мы используем библиотеку requests для получения
# html-страницы каждого сайта из списка urls. Затем мы записываем полученный
# текст в файл с именем, соответствующим названию сайта.

import requests # 🔥 Важно! Используйте pip install requests
import time
from os import chdir
chdir(fr'G:\YandexDisk\GB\Python\Flask и FastAPI\lesson_4_mnogozad')

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]

start_time = time.time()
for url in urls:
    response = requests.get(url)
    filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


# Downloaded https://www.google.ru/ in 0.46 seconds
# Downloaded https://gb.ru/ in 1.40 seconds
# Downloaded https://ya.ru/ in 1.93 seconds
# Downloaded https://www.python.org/ in 2.45 seconds
# Downloaded https://habr.com/ru/all/ in 3.08 seconds
