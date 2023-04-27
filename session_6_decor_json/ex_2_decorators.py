"""
2. A decorator that logs the arguments and return value of
a function. Function add called with args=(3, 4) returned 7.

We pass: add(3,4)
Output: 7 if we do the addition
"""

# Here's an example of a decorator that logs the arguments
# and return value of a function:

def log_func(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # print(f"Function {func.__name__} called with args={args} returned {result}")
        print(f"{func.__name__}{args}")
        return result
    return wrapper

# To use this decorator, you can simply apply it to any function
# that you want to log:

@log_func
def add(x, y):
    return x * y

result = add(3, 4)
print(result)

# Output: 12


