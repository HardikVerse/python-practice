'''Problem: Implement a decorator that caches the return values of a function, 
so that when it's called with the same arguments, the cached value is 
returned instead of re-executing the function.'''

import time


def cache(func):
    cache_strge = {}
    def wrapper(*args):
        if args in cache_strge:
            return cache_strge[args]
        result = func(*args)
        cache_strge[args] = result 
        return result
    return wrapper


@cache
def addition(*args):
    time.sleep(3)
    sum = 0
    for i in args:
        sum += i
    return sum


print(addition(4, 5, 6))
print(addition(4, 5, 6))
