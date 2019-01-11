'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the index of the first maximum of the sequence.

Example input
1
7
9
5
0

Example output
3
'''
max, idx, count = -1, 0, 0

while True:
    num = int(input())
    count += 1

    if num == 0:
        break

    if max < num:
        max = num
        idx = count

print(idx)
