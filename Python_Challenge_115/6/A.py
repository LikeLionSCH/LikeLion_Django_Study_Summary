'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the number of even elements of the sequence.

Example input
2
1
4
0

Example output
2
'''
count = 0

while True:
    num = int(input())

    if num == 0:
        break

    if num % 2 == 0:
        count += 1

print(count)
