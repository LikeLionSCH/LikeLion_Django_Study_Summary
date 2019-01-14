'''
Statement
Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, find the maximal element and print its row number and column number. If there are many maximal elements in different rows, report the one with smaller row number. If there are many maximal elements in the same row, report the one with smaller column number.

Example input
3 4
0 3 2 4
2 3 5 5
5 1 2 3
(maximal element is highlighted)

Example output
1 2
'''
col, row = map(int, input().split())
matrix, idx = [], [0, 0]

for i in range(col):
    matrix.append(list(map(int, input().split())))

max = matrix[0][0]

for i in range(col):
    for j in range(row):
        if matrix[i][j] > max:
            max = matrix[i][j]
            idx[0], idx[1] = i, j

print(idx[0], idx[1])
