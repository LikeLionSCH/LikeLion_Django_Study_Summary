'''
Statement
Given three integers, print them in ascending order.

Example input
5
3
7

Example output
3
5
7
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2:
    num1, num2 = num2, num1

if num1 > num3:
    num1, num3 = num3, num1

if num2 > num3:
    num2, num3 = num3, num2

print(num1)
print(num2)
print(num3)
