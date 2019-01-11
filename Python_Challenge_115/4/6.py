'''
Statement
In mathematics, the factorial of an integer n, denoted by n! is the following product:

n! = 1 × 2 × … × n

For the given integer n calculate the value n!. Don't use math module in this exercise.

Example input
4

Example output
24
'''
n = int(input())
result = 1

for i in range(1, n + 1):
    result *= i

print(result)
