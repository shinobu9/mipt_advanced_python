'''
Напишите декоратор, который принимает в качестве аргумента
путь к файлу. Если данный декоратор добавить к функции, то в
указанный файл будет логироваться информация вида:
Время вызова функции+
Входящие аргументы
Ответ return (если есть, если нет то логгировать '-')
Время завершения работы функции+
Время работы функции+
'''

import functools
import time

def output(path):
    def decorator_output(func):
        @functools.wraps(func)
        def wrapper_output(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            if value == None:
                value = '-'
            output = '\n'.join(list(map(str, [start_time, *args, *kwargs, value, end_time, run_time])))
            try:
                with open(path, 'w') as file:
                    file.write(output)
            except FileNotFoundError:
                print("No such directory, try again")
            except Exception:
                print("Unknown interrupt")
            return value
        return wrapper_output
    return decorator_output

@output(path="C:/Users/kamelis/Desktop/task4output.txt")
def summarizer(*integers):
    '''
    Summarize all given integers
    '''
    result = 0
    for i in integers:
        result += int(i)
    return result

if __name__ == "__main__":
    try:
        ints = list(map(int, input().split()))
        print(summarizer(*ints))
    except ValueError:
        print("Invalid type of input")
    except Exception:
        print("Unknown interrupt")
    
    
    