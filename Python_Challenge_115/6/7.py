'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the average of the sequence.

Example input
10
30
0

Example output
20.0
'''
sum, count = 0, 0

while True:
    num = int(input())

    if num == 0:
        break

    sum += num
    count += 1

print(sum / count)
