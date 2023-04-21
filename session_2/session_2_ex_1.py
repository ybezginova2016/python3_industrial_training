"""
1.Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters
(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

def computepay(hours, rate, *args, **kwargs):
    try:
        hours = float(hours)
        rate = float(rate)
    except ValueError:
        print("Error: hours and rate must be numeric values")
        return None

    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * rate * 1.5)

    return pay

hours = input("Enter hours: ")
rate = input("Enter rate: ")

pay = computepay(hours, rate)
if pay is not None:
    print("Pay:", pay)
