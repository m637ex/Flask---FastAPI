import requests
import threading # импорт потоков
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

def download (url):
    response = requests.get(url) 
    filename = 'threading_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text) # запишем в файл
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")
    
            

    
threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url]) # создаём отдельный поток для каждой ссылки
    threads.append(thread) # добавляем поток в список потоков
    thread.start() # Стартуем все потоки
for thread in threads:
    thread.join() # Ждем пока все потоки завершат свою работу
    


