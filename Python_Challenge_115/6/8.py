'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the maximum of the sequence.

Example input
1
2
3
2
1
0

Example output
3
'''
max = -1

while True:
    num = int(input())

    if num == 0:
        break

    if max < num:
        max = num

print(max)
