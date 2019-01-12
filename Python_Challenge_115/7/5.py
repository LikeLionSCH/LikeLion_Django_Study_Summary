'''
Statement
Given a list of numbers, determine and print the number of elements that are greater than both of their neighbors.

The first and the last items of the list shouldn't be considered because they don't have two neighbors.

Example input
1 5 1 5 1

Example output
2
'''
arr = list(map(int, input().split()))
count = 0

for idx, val in enumerate(arr):
    if idx == 0 or idx == len(arr) - 1:
        continue

    else:
        if val > arr[idx - 1] \
            and val > arr[idx + 1]:
            count += 1

print(count)
