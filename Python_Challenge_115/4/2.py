'''
Statement
Given two integers A and B. Print all numbers from A to B inclusively, in increasing order, if A < B, or in decreasing order, if A ≥ B.

Example input
8
5

Example output
8 7 6 5
'''
A = int(input())
B = int(input())

if A > B:
    for i in range(A, B - 1, -1):
        print(i, end=" ")

else:
    for i in range(A, B + 1):
        print(i, end=" ")
