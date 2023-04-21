mylist = []

print(type(mylist))
"""
Класс (class) – это тип данных. В Python тип (type) и класс (в большинстве слу-
чаев) являются синонимами. Объект (object) – это экземпляр (instance) класса.
Например, в Python есть класс списка list. Если я создаю список с именем mylist,
то mylist – это объект типа list.
"""
print(isinstance(mylist, list))
print(isinstance(mylist, str))

# Generator

def mygenerator(n):
    for i in range(n):
        yield i

print(type(mygenerator))
print(type(mygenerator(4)))