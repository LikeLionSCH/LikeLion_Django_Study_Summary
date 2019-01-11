'''
Statement
Given three integers, print the least of them.

Example input
5
3
7

Example output
3
'''
min = int(input())
num1 = int(input())
num2 = int(input())

if min > num1:
    min = num1

if min > num2:
    min = num2

print(min)
