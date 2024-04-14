from multiprocessing import Process # импорт процессов
import time
from pathlib import Path
from os import chdir
chdir(fr'G:\YandexDisk\GB\Python\Flask и FastAPI\sem_04_async')


dir_path = Path(r'G:\YandexDisk\GB\Python\Flask и FastAPI\sem_04_async')
file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
# print(file_paths)


def get_numbers_of_words_in_file (file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        lenght = 0
        for line in contents.split('\n'):
            line = line.replace('.',' ').replace(',',' ').replace('(',' ').replace(')',' ').replace('=',' ') \
                .replace('#',' ').replace('{',' ').replace('}',' ').replace('[',' ').replace(']', ' ') \
                .replace('/',' ').replace(':',' ').replace(';',' ').replace('_',' ').replace("'",' ') \
                .replace('"',' ')
            line = line.split()
            lenght += len(line)
            # print(f"{line = }; len: {len(line)}")
        print(f"Reading {file_path} in {time.time()-start_time:.2f} seconds. Len = {lenght}")
    
threads = []
start_time = time.time()

if __name__ == '__main__':
    for file_path in file_paths:
        thread = Process(target=get_numbers_of_words_in_file, args=[file_path]) # создаём отдельный поток для каждой ссылки
        threads.append(thread) # добавляем поток в список потоков
        thread.start() # Стартуем все потоки
    for thread in threads:
        thread.join() # Ждем пока все потоки завершат свою работу
    


