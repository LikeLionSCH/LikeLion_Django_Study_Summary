'''
Statement
Given a positive real number, print its first digit to the right of the decimal point.

Example input
1.79

Example output
7
'''
num = float(input())
print(int(num * 10 % 10))
