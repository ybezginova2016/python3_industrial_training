# for loop and if statement

List = [i for i in [1, 2, 3]]
print(List)

print([i**2 for i in [1, 4, 3]])

List = [i for i in range(11) if i % 2 == 0]
print(List)

matrix3 = [[j for j in range(3)] for i in range(3)]
matrix4 = [[j for j in range(3)] for i in range(4)]
matrix8 = [[j for j in range(8)] for i in range(4)]
print(matrix3)
print(matrix4)
print(matrix8)


List = []

for i in 'Hello':
    List.append(i)

print(List)
print([i for i in 'Hello'])


