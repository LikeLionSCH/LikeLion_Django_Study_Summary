'''
Statement
Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by two non-negative integers i and j less than n, swap the columns i and j of 2d list and print the result.

Example input
3 4
11 12 13 14
21 22 23 24
31 32 33 34
0 1

Example output
12 11 13 14
22 21 23 24
32 31 33 34
'''
col, row = map(int, input().split())
matrix = []

for _ in range(col):
    matrix.append(list(map(int, input().split())))

i, j = map(int, input().split())

for arr in matrix:
    arr[i], arr[j] = arr[j], arr[i]

print('\n'.join([' '.join([str(val) for val in arr]) \
                 for arr in matrix]))
