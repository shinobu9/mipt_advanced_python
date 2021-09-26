"""
Напишите функцию, которая получает на вход список чисел и выдает
ответ сколько в данном списке четных чисел.
Напишите декоратор, который меняет поведение функции следующим образом:
если четных чисел нет, то пишет "Нет(" а если их больше 10,
то пишет "Очень много"
"""

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        if value == 0:
            return "Нет("
        elif value > 10:
            return "Очень много"
        else:
            return func(*args, **kwargs)
    return wrapper_decorator


@decorator
def evencounter(arr):
    c = 0
    for i in arr:
        if i%2 == 0:
            c+=1
    return c

if __name__ == "__main__":
    listofnums = list(map(int, input().split()))
    print(evencounter(listofnums))