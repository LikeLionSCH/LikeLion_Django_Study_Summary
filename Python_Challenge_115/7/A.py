'''
Statement
Given a list of numbers, count a number of pairs of equal elements. Any two elements that are equal to each other should be counted exactly once.

Example input #1
1 2 3 2 3

Example output #1
2

Example input #2
1 1 1 1 1

Example output #2
10
'''
arr = input().split()
n, count = len(arr), 0

for i in range(0 , n):
    for j in range(i + 1, n):
        if (arr[i] == arr[j]):
            count += 1

print(count)
