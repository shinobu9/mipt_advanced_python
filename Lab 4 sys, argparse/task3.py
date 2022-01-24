'''
Напишите декоратор swap, который делает так, что задекорированная
функция принимает все свои неименованные аргументы в порядке,
обратном тому, в котором их передали (для аргументов с именем не вполне
правильно учитывать порядок, в котором они были переданы).
'''

import functools

def swap(func):
    @functools.wraps(func)
    def swap_wrapper(*args, **kwargs):
        args_reversed = []
        for i in range(len(args)-1, -1, -1):
            args_reversed.append(args[i])
        func(*args_reversed, **kwargs)
    return swap_wrapper

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 5, show=True)