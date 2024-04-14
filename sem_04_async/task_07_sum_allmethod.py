# Задание №7
# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

import random
import time
import asyncio
import threading
import multiprocessing


# Генерация массива из 1000000 случайных целых чисел
COUNT = 1000000
NUM_MIN = 1
NUM_MAX = 100

arr = [random.randint(NUM_MIN, NUM_MAX) for _ in range(COUNT)]

# Решение с использованием синхронности
start = time.time()
result = sum(arr)
print("Сумма элементов (синхронность):", result)
print("Время выполнения (синхронности):", time.time() - start)

# Решение с использованием многопоточности
def thread_sum(arr):
    result = sum(arr)
    print("Сумма элементов (многопоточность):", result)

start = time.time()
thread = threading.Thread(target=thread_sum, args=(arr,))
thread.start()
thread.join()
print("Время выполнения (многопоточность):", time.time() - start)

# Решение с использованием асинхронности
async def async_sum(arr):
    result = sum(arr)
    print("Сумма элементов (асинхронность):", result)

async def main():
    start = time.time()
    await async_sum(arr)
    print("Время выполнения (асинхронность):", time.time() - start)

asyncio.run(main())

# Решение с использованием многопроцессорности
def process_sum(arr):
    result = sum(arr)
    print("Сумма элементов (многопроцессорность):", result)

start = time.time()
if __name__ == '__main__':
    process = multiprocessing.Process(target=process_sum, args=(arr,))
    process.start()
    process.join()
    print("Время выполнения (многопроцессорность):", time.time() - start)
    




# import threading # импорт потоков
# from multiprocessing import Process 
# import asyncio
# import time
# from random import randint



    
# threads = []
# start_time = time.time()
# sum_arr = 0

# def sum_arr_thread(num):
#     global sum_arr
#     sum_arr += num
#     print(f'{num = }')

# for i in range(COUNT):
#     print(arr[i])
#     thread = threading.Thread(target=sum_arr_thread, args=arr[i]) # создаём отдельный поток для каждой ссылки
#     threads.append(thread) # добавляем поток в список потоков
#     thread.start() # Стартуем все потоки
# for thread in threads:
#     thread.join() # Ждем пока все потоки завершат свою работу
# print(f"Summa complate {sum_arr = } in {time.time()-start_time:.2f} seconds")