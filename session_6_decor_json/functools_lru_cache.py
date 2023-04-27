import functools

# функция Аккермана

@functools.lru_cache(maxsize=128) # хранит число последних вызовов
@functools.lru_cache(maxsize=None)
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3, 4)) # Output: 125
print(ackermann.cache_info())

"""
The Ackermann function is a classic example of a computable function that is not primitive recursive. 
It is named after Wilhelm Ackermann, a German mathematician who introduced it in 1928. 
The function is defined recursively as follows:

ackermann(m, n) =
    n + 1                     if m = 0
    ackermann(m - 1, 1)       if m > 0 and n = 0
    ackermann(m - 1, ackermann(m, n - 1))  if m > 0 and n > 0

The function takes two non-negative integer arguments m and n and returns a non-negative integer. 

The function is notable for being extremely fast-growing and for its ability to exceed the 
limitations of primitive recursion. In fact, the function grows so rapidly that its value 
for arguments greater than m=4 and n=2 are typically not practical to compute without 
the use of specialized algorithms and computer programs.

"""

print(ackermann(2, 3))  # Output: 9


