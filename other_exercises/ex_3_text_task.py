# TASK

"""
На вход программе подается список целых чисел, разделённых через пробел.
Напишите функцию, которая выведет на экран True, если в данном списке ровно
два вхождения числа 15 и не менее трех вхождений 4. Если нет, то False.
Вызовите функцию.

"""
a = input('Enter the range of integers: ')

nums = a.split()
# for num in nums:
#     print(int(num))

int_nums = [int(num) for num in nums]

def check_list(lst):
    nums = lst.split()
    int_nums = [int(num) for num in nums]

    count_15 = 0
    count_4 = 0
    for i in int_nums:
        if i == 15:
            count_15 += 1
        if i == 4:
            count_4 += 1
    if count_15 == 2 and count_4 >= 3:
        return True
    else:
        return False

print(check_list(a))
