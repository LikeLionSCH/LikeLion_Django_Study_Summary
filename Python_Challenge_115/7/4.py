'''
Statement
Given a list of non-zero integers, find and print the first adjacent pair of elements that have the same sign. If there is no such pair, print 0.

Example input #1
-1 2 3 -1 -2

Example output #1
2 3

Example input #2
1 -3 4 -2 1

Example output #2
0
'''
arr = list(map(int, input().split()))
check = False

for idx, val in enumerate(arr):
    if idx == 0:
        continue

    else:
        if (val > 0 and arr[idx - 1] > 0) \
            or (val < 0 and arr[idx - 1] <0):
            print(arr[idx - 1], val)
            check = True
            break

if not check:
    print(0)
