def print_map(function, iterable):
    for i in iterable:
        print(function(i))
        
def print_map1(function, iterable):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            function(item)
    
def function(integer):
    return integer ** 2

def iter_fib(n):
    _last = 0
    _current = 1
    while n>0:
        yield _current
        _current, _last = _current + _last, _current
        n -= 1

a = [1,2,3,4,5]
#print_map(function, a)

for i in iter_fib(5):
    print(i)