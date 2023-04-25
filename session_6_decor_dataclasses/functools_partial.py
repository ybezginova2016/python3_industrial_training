# Not a decorator
# Function partial
import functools

f = functools.partial(sorted, key=lambda p: p[1])
print(f)

"""
The functools.partial function is a higher-order function in Python that allows you to "partially apply" arguments to a function, which creates a new function that can be called with the remaining arguments.

In the example you provided, functools.partial(sorted, key=lambda p: p[1]) creates a new function called f that sorts a sequence of elements by their second item. The sorted function normally takes a sequence as its first argument and an optional key function as its second argument. The key function is used to extract a value from each element in the sequence, which is then used to determine the sort order.

By using functools.partial to apply the key=lambda p: p[1] argument to sorted, the resulting f function can be called with a sequence of elements to sort based on the second item of each element
"""
elements = [(1, 3), (2, 1), (3, 2)]
print(f(elements)) # Output: [(2, 1), (3, 2), (1, 3)]
