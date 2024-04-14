# Многопоточность Пример 1:
import multiprocessing # многопроцессорность
import threading # многопоточность
import time


"""
def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")

if __name__ == '__main__':
    processes = []  # список потоков
    for i in range(5):  # 5 - это 5 потоков
        # модуль отвечает за работу с потоками,
        p = multiprocessing.Process(target=worker, args=(i, ))
        # ф-ия worker работает внутри потока
        # args - аргументы ф-кции worker
        processes.append(p)  # добавляем поток t  в список потоков
        p.start()  # старрует работы функций

    for p in processes:
        p.join()

    print("Все потоки завершили работу")
"""
    

# # Многопоточность пример 2 последовательная работа потоков
# def worker(num):
#     print(f"Начало работы потока {num}")
#     time.sleep(3)
#     print(f"Конец работы потока {num}")

# if __name__ == '__main__':
#     processes = []  # список потоков
#     for i in range(5):  # 5 - это 5 потоков
#         # модуль отвечает за работу с потоками,
#         p = multiprocessing.Process(target=worker, args=(i, ))
#         # ф-ия worker работает внутри потока
#         # args - аргументы ф-кции worker
#         processes.append(p)  # добавляем поток t  в список потоков

#     for p in processes:
#         p.start()  # стартует работы функций о очереди
#         p.join()

#     print("Все потоки завершили работу")



   
# Многопоточность Привет 3
# counter = 0

# def increment():
#     global counter
#     for _ in range(1_000_000):
#         counter += 1    
#     print(f"Значение счетчика: {counter:_}")

# if __name__ == '__main__':
#     processes = []
#     for i in range(5):
#         p = multiprocessing.Process(target=increment)
#         processes.append(p)
#         p.start()
#     for p in processes:
#         p.join()
#     print(f"Значение счетчика в финале: {counter:_}")

# =>
# Значение счетчика: 1_000_000
# Значение счетчика: 1_000_000
# Значение счетчика: 1_000_000
# Значение счетчика: 1_000_000
# Значение счетчика: 1_000_000
# Значение счетчика в финале: 0


# пример 4
# 5 процессов используя доступ к одному объекту увеличивают его значение
# до 50 тысяч — 5 процессов по 10к каждый.
import multiprocessing

counter = multiprocessing.Value('i', 0) # 'i' - сокращение от Integer, 0 - начальное значение
# переменная counter взаимодейстуем между разными процессами

def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock(): #  На время выполнения операции мы блокируем значение переменной от изменений другими процессорами
            cnt.value += 1
    print(f"Значение счетчика: {cnt.value:_}")
    
if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment,
        args=(counter, ))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f"Значение счетчика в финале: {counter.value:_}")

# =>
# Значение счетчика: 11_532
# Значение счетчика: 40_142
# Значение счетчика: 47_314
# Значение счетчика: 49_376
# Значение счетчика: 50_000
# Значение счетчика в финале: 50_000