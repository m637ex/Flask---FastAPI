# Задание №9
# � Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. 
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию 
# изображения в URL-адресе.
# � Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# � Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# � Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# � Программа должна выводить в консоль информацию о времени скачивания каждого изображения и 
# общем времени выполнения программы.
import requests
import time
import threading
import multiprocessing
import asyncio




urls = [   
    'https://i.pinimg.com/564x/b2/4e/6e/b24e6e3c3c15b8f29377faeb610d8658.jpg',
    'https://i.pinimg.com/736x/14/09/0b/14090b36c0a458791a69f00d34d1b921.jpg',
    'https://i.pinimg.com/564x/ea/51/1b/ea511ba724d110e89185e7d941ca53e8.jpg',
    'https://i.pinimg.com/564x/aa/24/44/aa2444896411c1be9a020c584e51c3eb.jpg',
    'https://i.pinimg.com/564x/8e/18/d4/8e18d42e9f7dbe392b2fdb61ed155cfc.jpg',
    'https://i.pinimg.com/564x/f7/56/99/f75699247c6ea6d637bddb3254b3111d.jpg',
    'https://i.pinimg.com/564x/99/02/28/99022851a5e07432b39aaa6cc4c8b25d.jpg',
    'https://i.pinimg.com/564x/ed/8e/17/ed8e1762e710e921f0ba7c1c2bd1d11b.jpg',
    'https://i.pinimg.com/564x/fe/d4/e9/fed4e95f98740e4f120160a3c8931e00.jpg',
    'https://i.pinimg.com/564x/f7/5d/62/f75d621465d8766dd1191db7b5b2759a.jpg',
]

def thread_get_image(url):
    response = requests.get(url) 
    filename = 'threading_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    if response.status_code == 200:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.content)            
            
    
threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=thread_get_image, args=[url]) # создаём отдельный поток для каждой ссылки
    threads.append(thread) # добавляем поток в список потоков
    thread.start() # Стартуем все потоки
for thread in threads:
    thread.join() # Ждем пока все потоки завершат свою работу