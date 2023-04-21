"""
1.Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

"""

hours = int(input('Please enter the number of working hours: '))
if hours <= 40:
    rate = 10
    print(f'Your salary is:', hours * rate)
elif hours > 40:
    rate = 10
    rate_new = rate * 1.5
    print(f'Your salary is:', hours * rate_new)


try:
    hours = int(input('Please enter the number of working hours: '))
except ValueError:
    print("Sorry, this is not an integer. Please insert an integer.")
else:
    if hours <= 40:
        rate = 10
        print(f'Your salary is: {hours * rate}')
    elif hours > 40:
        rate = 10
        rate_new = rate * 1.5
        print(f'Your salary is: {hours * rate_new}')

