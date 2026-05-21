'''Problem: Write a decorator that measures the time a 
function takes to execute.'''


import time

def cal_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        stop = time.time()
        print(f"{func.__name__} run in {stop-start:.2f} seconds.")
        return result
    return wrapper


@cal_time
def ex_func():
    time.sleep(2)
    return "Done"

ex_func()
print(ex_func())