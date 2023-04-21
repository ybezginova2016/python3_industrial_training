# Exception Handling

try:
    hours = int(input("Please enter the number of working hours: "))
    if hours <= 40:
        rate = 10
        print("Your salary is:", hours * rate)
    else:
        rate = 10
        rate_new = rate * 1.5
        print("Your salary is:", hours * rate_new)
except ValueError:
    print("Invalid input. Please enter a valid integer for the number of working hours.")
