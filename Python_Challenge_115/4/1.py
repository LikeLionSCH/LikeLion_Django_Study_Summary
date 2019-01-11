'''
Statement
Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

Example input
1
10

Example output
1 2 3 4 5 6 7 8 9 10
'''
A = int(input())
B = int(input())

for i in range(A, B + 1):
    print(i, end=" ")
