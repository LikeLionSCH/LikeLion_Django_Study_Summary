'''
Statement
Given a list of distinct numbers, swap the minimum and the maximum and print the resulting list.

Example input
3 4 5 2 1

Example output
3 4 1 2 5
'''
arr = list(map(int, input().split()))

min_idx, max_idx = arr.index(min(arr)), arr.index(max(arr))
arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]

print(' '.join(map(str, arr)))
