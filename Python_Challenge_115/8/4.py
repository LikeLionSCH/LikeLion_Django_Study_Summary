'''
Statement
Given an integer n, create a two-dimensional array of size n×n according to the following rules and print it:

On the antidiagonal put 1.
On the diagonals above it put 0.
On the diagonals below it put 2.

Example input
4

Example output
0 0 0 1
0 0 1 2
0 1 2 2
1 2 2 2
'''
num = int(input())

for i in range(num):
    for j in range(num):
        if i + j < (num - 1):
            print("0", end=" ")

        elif i + j == (num - 1):
            print("1", end=" ")

        else:
            print("2", end=" ")
    print()
