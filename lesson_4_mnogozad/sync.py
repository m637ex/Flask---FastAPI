import time

# пример 1 инхронное выполнение кода:
def count_down(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
        
count_down(5)


# пример 2 синхронное выполнение кода:
import time
def slow_function():
    print("Начало функции")
    time.sleep(5)
    print("Конец функции")
    
print("Начало программы")
slow_function()
print("Конец программы")


# пример 3 синхронное выполнение кода:
import random
import time
def long_running_task():
    for i in range(5):
        print(f"Выполнение задачи {i}")
        time.sleep(random.randint(1, 3))
        
def main():
    print("Начало программы")
    long_running_task()
    print("Конец программы")
    
main()


# !!! Многопоточный подход !!!