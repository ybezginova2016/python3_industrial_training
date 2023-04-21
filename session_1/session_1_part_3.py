# try and except

try:
    print(x)
except:
    print('An exception occured')

# print(x)
print('string')


try:
    print(x)
except NameError:
    print('Variable is not defined')
else:
    print('Something went wrong')

x = 1

while x < 128:
    print(x, end=' ')
    x = x * 2
print()
x = 'not a number'
try:
    f = float(x)
except ValueError:
    print('You can not do that!')