import asyncio # импорт асинхронной библиотеки
import time
from pathlib import Path
from os import chdir
chdir(fr'G:\YandexDisk\GB\Python\Flask и FastAPI\sem_04_async')


dir_path = Path(r'G:\YandexDisk\GB\Python\Flask и FastAPI\sem_04_async')
file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
# print(file_paths)


async def get_numbers_of_words_in_file (file_path):
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
    

start_time = time.time()

async def main():
    tasks = []
    for file_path in file_paths:
        task = asyncio.ensure_future(get_numbers_of_words_in_file(file_path)) # создаём отдельный поток для каждой ссылки
        tasks.append(task) # добавляем поток в список потоков
    await asyncio.gather(*tasks) # выполни все задачи одновременно асинхронно
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop() # в переменную loop получаем цикл событий
    loop.run_until_complete(main()) # цикл событий, запусти корутину main до тех пор пока она не завершится.

