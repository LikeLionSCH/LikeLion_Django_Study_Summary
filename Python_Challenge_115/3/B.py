'''
Statement
Given three integers, in which two are equal to each other and the third one is different. Print the order number of this different one - 1, 2 or 3.

Example input #1
10
5
10

Example output #1
2

Example input #2
10
10
5

Example output #2
3
'''
num1 = input()
num2 = input()
num3 = input()

if num1 == num2:
    print(3)

elif num1 == num3:
    print(2)

else:
    print(1)
