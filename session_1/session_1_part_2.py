# Boolean
x = 8
y = 8.4
z = '8'

print(x == y) # x is equal to y
print(x != y)
print(x is not y) # they are not the same in the memory

print(x == int(z))

x = 0
print(isinstance(x, list))

# conditional execution
x = 0
if x >= 0:
    print('x is positive')
else:
    print('either 0 or neg')

# conditional execution
x = 0
if x >= 0:
    pass
else:
    print('either 0 or neg')

