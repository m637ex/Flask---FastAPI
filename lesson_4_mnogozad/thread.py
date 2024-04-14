# Многопоточность Пример 1:
import multiprocessing # многопроцессорность
import threading # многопоточность
import time


"""
def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")


threads = []  # список потоков
for i in range(5):  # 5 - это 5 потоков
    # модуль отвечает за работу с потоками,
    t = threading.Thread(target=worker, args=(i, ))
    # ф-ия worker работает внутри потока
    # args - аргументы ф-кции worker
    threads.append(t)  # добавляем поток t  в список потоков
    t.start()  # старрует работы функций

for t in threads:
    t.join()

print("Все потоки завершили работу")


# Многопоточность пример 2 последовательная работа потоков
def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")


threads = []  # список потоков
for i in range(5):  # 5 - это 5 потоков
    # модуль отвечает за работу с потоками,
    t = threading.Thread(target=worker, args=(i, ))
    # ф-ия worker работает внутри потока
    # args - аргументы ф-кции worker
    threads.append(t)  # добавляем поток t  в список потоков

for t in threads:
    t.start()  # стартует работы функций о очереди
    t.join()

print("Все потоки завершили работу")


# Многопоточность Пример 3:
def worker(num):
    print(f"Запущен процесс {num}")
    time.sleep(3)
    print(f"Завершён процесс {num}")
    
processes = []
for i in range(5):
    p = threading.Thread(target=worker, args=(i,))
    processes.append(p) # добавляем поток t  в список потоков
for p in processes:
    p.start()
    p.join()
print("Все процессы завершили работу")
"""

    
# Многопоточность Привет 4
counter = 0

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1    
    print(f"Значение счетчика: {counter:_}")

processes = []
for i in range(5):
    p = threading.Thread(target=increment)
    processes.append(p)
    p.start()
for p in processes:
    p.join()
print(f"Значение счетчика в финале: {counter:_}")
