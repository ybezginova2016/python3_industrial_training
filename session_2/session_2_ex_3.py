"""
# problem
print('Good morning!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good afternoon!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good evening!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')

"""

def ask_feeling(time_of_day):
    while True:
        try:
            print('Good ' + time_of_day + '!')
            print('How are you feeling?')
            feeling = input()
            if not feeling:
                raise ValueError('You did not enter anything.')
            break
        except ValueError as e:
            print('Error:', e)
    return feeling

for time_of_day in ['morning', 'afternoon', 'evening']:
    feeling = ask_feeling(time_of_day)
    print('I am happy to hear that you are feeling ' + feeling + '.')
