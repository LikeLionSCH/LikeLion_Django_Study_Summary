'''
Statement
Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Given a positive integer n, print the nth Fibonacci number.

Example input
6

Example output
8
'''
num = int(input())
before, curr, i = 0, 1, 1

while num > i:
    before, curr = curr, curr + before
    i += 1

print(curr)
