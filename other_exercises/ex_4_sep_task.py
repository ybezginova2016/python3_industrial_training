### TASK ###
"""
Программе на вход поступает строка. Нужно написать программу, которая
будет проверять присутствует ли разделитель в виде пробела или запятой
и разбивать её по заданному разделителю. Гарантируется, что в качестве
разделителя выступает только запятая или пробел.

Если разделители отсутствуют, то следует вывести все символы,
которые имеют четное число при переводе в Юникод.

На экран требуется вывести список.
"""

s = input('Enter a sentence, phrase or just a word: ')
separators = ' ,'
for sep in separators:
    words = s.replace(sep, '')

# выбираем только символы с четными кодами
words_uni = filter(lambda c: ord(c) % 2 == 0, words)

# проверяем, что строка не пустая
if words_uni:
    print(''.join(words_uni))
else:
    print('No even characters found')

"""
Здесь мы используем функцию filter для выбора только символов с четными кодами. 
Затем мы преобразуем результат в строку с помощью метода join. Если строка пустая, 
то выводим сообщение об отсутствии символов, удовлетворяющих условиям задачи.
"""

s = input('Enter a sentence, phrase or just a word: ')
def unicode_check(s):
    separators = ' ,'
    for sep in separators:
        s = s.replace(sep, '')
    words_uni = [c for c in s if ord(c) % 2 == 0]
    if words_uni:
        return words_uni
    else:
        return 'No even characters found'

print(unicode_check(s))