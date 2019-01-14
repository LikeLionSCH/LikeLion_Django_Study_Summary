'''
Statement
Given two positive integers n and m, create a two-dimensional array of size n×m and populate it with the characters "."and "*" in a chequered pattern. The top left corner should have the character "." .

Example input
6 8

Example output
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
'''
n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0:
                print('.', end=" ")

            else:
                print('*', end=" ")

        else:
            if j % 2 == 0:
                print('*', end=" ")

            else:
                print(".", end=" ")

    print()
