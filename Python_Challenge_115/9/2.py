'''
Statement
Given two lists of numbers, count how many numbers of the first one occur in the second one.

Example input
1 3 2
4 3 2

Example output
2
'''
arr1 = list(set(input().split()))
arr2 = input().split()

print(len([val for val in arr1 if val in arr2]))
