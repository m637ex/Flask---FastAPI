# # Пример 1
# import asyncio # модуль асинхронного вывода ввода данных

# async def print_numbers(): # корутина 1
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(1) #await осуществляется ожидание выполнения операции asyncio.sleep()
        
# async def print_letters(): # корутина 2
#     for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
#         print(letter)
#         await asyncio.sleep(0.5) #await осуществляется ожидание выполнения операции asyncio.sleep()
        
# async def main():   # В функции main() создаются две задачи, которые выполняются параллельно, а затем ожидается их завершение.
#     task1 = asyncio.create_task(print_numbers())
#     task2 = asyncio.create_task(print_letters())
#     await task1
#     await task2
    
# asyncio.run(main()) # создаём цикл событий 'main()'
# # => 0 a b 1 c d 2 e f 3 4 5 6 7 8 9 

# Пример 2:
# import asyncio
# async def count(): # корутина
#     print("Начало выполнения")
#     await asyncio.sleep(1)
#     print("Прошла 1 секунда")
#     await asyncio.sleep(2)
#     print("Прошло еще 2 секунды")
#     return "Готово"

# async def main():
#     result = await asyncio.gather(count(), count(), count()) # count() запускаем обновременно 3 раза
#     print(result)
    
# asyncio.run(main())  # создаём цикл событий 'main()'

#Начало выполнения
# Начало выполнения
# Начало выполнения
# Прошла 1 секунда
# Прошла 1 секунда
# Прошла 1 секунда
# Прошло еще 2 секунды
# Прошло еще 2 секунды
# Прошло еще 2 секунды
# ['Готово', 'Готово', 'Готово']


# пример 3
import asyncio
from pathlib import Path

async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        # do some processing with the file contents
        print(f'{f.name} содержит {contents[:7]}...')
        
async def main():
    dir_path = Path(r'G:\YandexDisk\GB\Python\Flask и FastAPI\lesson_4_mnogozad')
    #dir_path = Path('.')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths] # создаём новую корутину asyncio.create_task(process_file(file_path)
    await asyncio.gather(*tasks) # запуск созданных выше корутин tasks
if __name__ == '__main__':
    asyncio.run(main())
