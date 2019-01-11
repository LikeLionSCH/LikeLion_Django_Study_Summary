'''
Statement
Given an integer not less than 2. Print its smallest integer divisor greater than 1.

Example input
15

Example output
3
'''
num = int(input())
i = 2

while num % i != 0:
    i += 1

print(i)
