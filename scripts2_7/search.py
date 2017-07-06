import os

def find(name):
    for root, dirs, files in os.walk(os.getcwd()):
        if name in files:
            return os.path.join(root, name)
        

print (find('tetgen'))
