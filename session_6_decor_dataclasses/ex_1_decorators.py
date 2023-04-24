"""
1.Create a decorator called timeit that prints out the time a
function takes to execute in seconds. Your timeit decorator
should work with any function that returns a value, regardless
of the number of arguments it takes.

2. Write a decorator that repeats a function call a specified number
of times. Imagine you have a function that prints hello world,
but using a decorator you should be able to repeat that process
3 times.
"""

import time

def repeat(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello World!")

say_hello()

