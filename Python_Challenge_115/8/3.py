'''
Statement
Given an integer n, create a two-dimensional array of size n×n according to the following rules and print it:

On the main diagonal put 0.
On the diagonals adjacent to the main put 1.
On the next adjacent diagonals put 2, and so forth.

Example input
5


Example output
0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
'''
num = int(input())

for i in range(num):
    for j in range(num):
        print(abs(i - j), end=" ")
    print()
