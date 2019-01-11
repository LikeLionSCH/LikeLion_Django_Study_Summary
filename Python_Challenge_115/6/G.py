'''
Statement
Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Given a positive integer, determine if it's the nth Fibonacci number for some n. If it is, print such n, otherwise print -1.

Example input
8

Example output
6
'''
num = int(input())
before, curr, count = 0, 1, 1

while curr < num:
    before, curr = curr, before + curr
    count += 1

print(count) if curr == num else print(-1)
