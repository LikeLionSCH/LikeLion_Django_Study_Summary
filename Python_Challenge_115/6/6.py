'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the sum of the sequence.

Example input
1
7
9
0

Example output
17
'''
sum = 0

while True:
    num = int(input())

    if num == 0:
        break

    sum += num

print(sum)
