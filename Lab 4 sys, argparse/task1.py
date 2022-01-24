"""
Напишите консольную программу, которой на вход подается
единственное число N (без имени или с именем -n),
а программа печатает значение Nго числа Фибоначчи
"""
import sys
import argparse
import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    return parser

if __name__ == "__main__":
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])

    print (fib(int(namespace.n)))