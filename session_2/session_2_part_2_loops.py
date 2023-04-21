# while loop

n = 5

# infinite loop
while n > 0:
    print(n)
    # n += 1 # infinite loop
    n -= 1
print('Finished!')

# pass - just lets the code go further
# continue - just ignores the rest of the program, and start the loop from the begininng

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
