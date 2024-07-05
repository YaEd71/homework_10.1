import threading
from time import sleep

def print_numbers():
    for i in range(1, 11):
        print(i)
        sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        sleep(1)

# Создание потоков
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Запуск потоков
thread1.start()
thread2.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()

print("Оба потока завершены.")