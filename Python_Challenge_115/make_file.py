import os

dir = input("Enter the foler name : ")
num = int(input("Enter the number of python file : "))

os.chdir(os.getcwd() + "/" + dir)

for i in range(1, num + 1):
    if i < 10:
        file = open(str(i) + ".py", "w")

    else:
        file = open(chr(ord("A") + ((i - 1) % 9)) + ".py", "w")

file.close()
