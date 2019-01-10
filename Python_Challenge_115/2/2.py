'''
Statement
Given a two-digit integer, swap its digits and print the result.

Example input
79

Example output
97
'''
a = int(input())
print(str(a % 10) + str(a // 10))
