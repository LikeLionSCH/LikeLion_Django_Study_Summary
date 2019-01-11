'''
Statement
For a given integer N, print all the squares of positive integers where the square is less than or equal to N, in ascending order.

Example input
50

Example output
1 4 9 16 25 36 49
'''
num = int(input())
i = 1

while i ** 2 <= num:
     print(i ** 2, end=' ')
     i += 1
