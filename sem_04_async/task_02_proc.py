import requests
from multiprocessing import Process, Pool
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
    filename = 'multiprocessing_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text) # запишем в файл
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")
    
processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=[url]) # создаём отдельный поток для каждой ссылки
        processes.append(process) # добавляем поток в список потоков
        process.start() # Стартуем все потоки
    for process in processes:
        process.join() # Ждем пока все потоки завершат свою работу
    


