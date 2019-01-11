'''
Statement
Given five integers, print the least of them.

Example input
10
20
30
40
50

Example output
10
'''
min = int(input())
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if min > num1:
    min = num1

if min > num2:
    min = num2

if min > num3:
    min = num3

if min > num4:
    min = num4

print(min)
