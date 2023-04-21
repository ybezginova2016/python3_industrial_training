f = open("C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\hello_world.txt")
print(f.readline())

for x in f:
    print(x)
f.close()

# writing to files

f = open("C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\hello_world.txt", 'w')
f.write("OVERWRITE.")
f.close()
