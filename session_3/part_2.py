import os

path = "C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\hello_world.txt"
if os.path.exists(path):
    os.remove(path)
else:
    print('FileNotFound')