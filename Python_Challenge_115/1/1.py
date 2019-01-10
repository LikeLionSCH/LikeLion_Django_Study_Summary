'''
Statement
Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

Example input
2
3
6

Example output
11
'''
sum = 0

for _ in range(3):
    sum += int(input())

print(sum)
