# Применение нескольких декораторов
# Порядок декораторов имеет значение

def square(func):
    return lambda x: func(x * x)

def addsome(func):
    return lambda x: func(x + 2)

@square
@addsome

def identity(x):
    return x

print(identity(2))

@addsome
@square
def identity(x):
    return x
print(identity(2))
