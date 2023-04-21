fruits = ['apple', 'banana', 'cherry']

for i in fruits:
    print(fruits[2])

for i in 'test':
    print(i)

for x in fruits:
    print(x)
    if x == 'banana':
        break

for i in fruits:
    # print(x)
    if x == 'banana':
        print(i)

total = 0
for itervar in [3, 41, 12, 9, 75]:
    total = total + itervar
print('Total: ', total)