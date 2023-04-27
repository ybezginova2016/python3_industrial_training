# Join Zoom Meeting at 7 PM (GMT+2)
# https://us06web.zoom.us/j/81012729169?pwd=WEIxUEczbWV6YlJwaGlFTUlYaTYyQT09
#
# Meeting ID: 810 1272 9169
# Passcode: 441609

#### Defining a variable

print(type('4'))
print(type(4))
print(type(4.0))

print(1,000) # 2 arguments, 2 numbers - 1 and 0

# variables

c = True
print(type(c))
print(c) # gives a value of c variable

c = [1, 2, 3, 4, 5, 6, 7]
print(c)
print(type(c))

x = 5
print(id(x))
x = 'string'
print(x)
print(x)

name = 'John'
age = 30

# concenation is not possbile with different types
# we can concetinate only the same types - string
print('My name is ' + name + ' and I am ' + str(age) + ' years old.')
print('My name is', name, 'and I am', age, 'years old.')
print(f"My name is {name} and I am {age} years old.")

person = {'name' : 'Jane',
          'age' : 25,
          'city' : 'New York'}

print('Jane is ' + str(person['age']) + ' years old.')

quotient = 7 // 3
print(quotient)

quotient = 7 / 3
print(quotient)

x = 1234567
remainder = x % 10
print(remainder)

"""
Task: Determine if the variable x is odd or even using the modulus operator (%) with respect to the value of y.

Solution:

Assign values to the variables x and y.
Use the modulus operator % to calculate the remainder of x divided by y, and store the result in a variable called remainder.
Check if the remainder is equal to zero. If it is, print "x is an odd". Otherwise, print "x is an even".
Note that the solution given assumes that the print statements in the original code have been incorrectly labeled, and that the code is actually checking whether x is odd or even, not vice versa.
"""

x = 10
y = 3

remainder = x % y

if remainder == 0:
    print(x, 'is an odd')
else:
    print(x, 'is an even')


