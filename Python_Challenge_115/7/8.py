'''
Statement
Given a list of integers, find the first maximum element in it. Print its value and its index (counting with 0).

Example input
1 2 3 2 1

Example output
3 2
'''
arr = list(map(int, input().split()))

print(max(arr), arr.index(max(arr)))
