'''
Statement
Given a three-digit number. Find the sum of its digits.

Example input
123

Example output
6
'''
num = int(input())
print(num // 100
      + num % 100 // 10
      + num % 10)
