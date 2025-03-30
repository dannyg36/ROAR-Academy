import os
path = os.path.dirname(os.path.abspath(__file__))
f = open(path + '/' + "motto.txt", "w")
f.write("Fiat Lux!\n")
f.close()
f = open(path + '/' + "motto.txt", "a")
f.write("Let there be light!")
f = open(path + "/motto.txt", "r")
print(f.read())

