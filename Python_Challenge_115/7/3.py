'''
Statement
Given a list of numbers, find and print all its elements that are greater than their left neighbor.

Example input
1 5 2 4 3

Example output
5 4
'''
arr = input().split()

for idx, val in enumerate(arr):
    if idx == 0:
        continue

    else:
        if arr[idx - 1] < val:
            print(val, end=' ')
