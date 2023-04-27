"""
3. Create a decorator timer that times the execution of a
function and outputs the time taken to the console.

Function my_function took 1.0011944770812988 seconds to execute
and this execution time is something variable

every time you would get a different result
"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result
    return wrapper

@timer
def my_func(x, y):
    time.sleep(2)
    return x + y

result = my_func(2, 3)
print(result)