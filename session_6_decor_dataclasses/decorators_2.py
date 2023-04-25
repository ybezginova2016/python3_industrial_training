def decorate(func):
    print(f"In 'decorate' function, we decorate:", func.__name__)
    def wrapper_func(*args, **kwargs):
        print('Executing:', func.__name__)
        return func(*args)

    return wrapper_func

def myfunction(parameter):
    print(parameter)

print(decorate(myfunction))
print(myfunction("hello"))