'''
Statement
For a given integer X, find the greatest integer n where 2ⁿ is less than or equal to X. Print the exponent value and the result of the expression 2ⁿ.

Example input
50

Example output
5 32
'''
X = int(input())
n = 0

while X >= 2 ** (n + 1):
    n += 1

print(n, 2 ** n)
