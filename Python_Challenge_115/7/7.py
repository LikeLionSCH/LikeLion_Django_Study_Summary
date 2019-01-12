'''
Statement
Given a list of numbers, swap adjacent elements in each pair (swap A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element intact.

Example input
1 2 3 4 5

Example output
2 1 4 3 5
'''
arr = input().split()

if len(arr) % 2 == 0:
    for idx in range(0, len(arr), 2):
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

else:
    for idx in range(0, len(arr) - 1, 2):
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

print(' '.join(arr))
