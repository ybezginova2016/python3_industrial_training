"""
1.Write a program to prompt the user for hours and rate per
hour to compute gross pay.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

"""
# input method is a string by default!

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = hours * rate

print("Pay:", pay)

# or
hours = input("Enter Hours: ") # string
rate = input("Enter Rate: ") # string
pay = int(hours) * int(rate)
print(pay)

# or
hours = input("Enter Hours: ") # string
rate = input("Enter Rate: ") # string
pay = float(hours) * float(rate)
print(pay)