'''
Statement
Given two lists of numbers, find all the numbers that occur in both the first and the second list. Print them in ascending order.

Example input
1 3 2
4 3 2

Example output
2 3
'''
arr1 = sorted(list(map(int, input().split())))
arr2 = list(map(int, input().split()))

print(' '.join([str(val) for val in arr1 if val in arr2]))
