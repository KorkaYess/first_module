# домашка при установке виртуального окружения
import time


def timer(func):
    def wrapper(*args, **kwargs):
        a = time.perf_counter()
        print(func(*args, **kwargs))
        b = time.perf_counter()
        return b - a

    return wrapper

@timer
def filler(x):
    time.sleep(x)

print(filler(5))
