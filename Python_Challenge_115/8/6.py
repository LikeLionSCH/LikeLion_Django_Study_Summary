'''
Statement
Given an odd positive integer n, produce a two-dimensional array of size n×n. Fill each element with the character "." . Then fill the middle row, the middle column and the diagonals with the character "*".  You'll get an image of a snow flake. Print the snow flake in n×n rows and columns and separate the characters with a single space.

Example input
7

Example output
* . . * . . *
. * . * . * .
. . * * * . .
* * * * * * *
. . * * * . .
. * . * . * .
* . . * . . *
'''
num = int(input())

for i in range(num):
    for j in range(num):
        if i == j or (i + j) == (num - 1):
            print('*', end=" ")

        elif i == (num // 2):
            print('*', end=" ")

        elif j == (num // 2):
            print('*', end=" ")

        else:
            print('.', end=" ")

    print()
