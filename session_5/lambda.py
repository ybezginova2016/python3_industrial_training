# a = 7
# def fun():
#     return a + 10
# print(fun(5))

# lambda arguments: expression

x = lambda a: a + 10
print(x(7))

y = lambda a, b: (a + 10, b - 8)
result = y(7, 8)
print(result)
