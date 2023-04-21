import random
t = [1, 2, 3, 4, 5]
print(random.choice(t))

"""
The built-in function print(random.choice(t)) does the following:

random.choice(t): This part of the code selects a random element from the list t. 
The random.choice() function is part of the random module and takes a sequence 
(like a list) as an argument.

print(...): The print() function takes the result of random.choice(t) and displays 
it as output. In this case, it will print the randomly selected element from the 
list t.

So, the whole line print(random.choice(t)) prints a random element from the 
list t to the console.
"""

def myFun(arg1, arg2, arg3, *args): # I can pass as many arguments as I want
    print('First argument: ', arg1)
    for arg in args:
        print('Next argument through *argv :', arg)

myFun('Hello', 'welcome', 'to', 'class')

# args = ('This', 'is', 'demo')
# myFun(*args)

def myFun(arg1, arg2, arg3, *kwargs):
    print('First argument: ', arg1)
    for arg in kwargs:
        print('Next argument through *kwargs:', arg)

kwargs = {'arg1': 'This', 'arg2' : 'is', 'arg3': 'demo.'}
myFun(**kwargs)


def my_function(*kids):
    print('The youngest child is ' + kids[2])

my_function('Emil', 'Tobias', 'Linus')