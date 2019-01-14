'''
Statement
Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by one integer c. Multiply every element by c and print the result.

Example input
3 4
11 12 13 14
21 22 23 24
31 32 33 34
2

Example output
22 24 26 28
42 44 46 48
62 64 66 68
'''
col, row = map(int, input().split())
matrix = []

for i in range(col):
    matrix.append(list(map(int, input().split())))

c = int(input())

for i in range(col):
    for j in range(row):
        print(matrix[i][j] * c, end=' ')
    print()
