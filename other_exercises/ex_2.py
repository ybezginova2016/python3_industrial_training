# def my_func():
#     """
#     This code defines a generator function called my_func() that uses
#     a for loop and yield statements to generate a sequence of values from 0 to 11.
#     :return:
#     """
#     for i in range(12):
#         yield i
#
# x = my_func()
#
# for _ in range(6):
#     x = next(x)
#
# print(x)

# The error is caused by reassigning x to the value returned by next(x),
# which is an integer, instead of the generator object returned by my_func().
# To correct the error, you should use a different variable to store
# the result of next(x) and leave x as the generator object.

def my_func():
    """
    This code defines a generator function called my_func() that uses
    a for loop and yield statements to generate a sequence of values from 0 to 11.
    :return:
    """
    for i in range(12):
        yield i

x = my_func()

for _ in range(6):
    next(x)

print(next(x))