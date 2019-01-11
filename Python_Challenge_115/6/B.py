'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the number of elements of the sequence that are greater than their neighbors above.

Example input
1
2
3
4
5
0

Example output
4
'''
count = -1

while True:
    if count == -1:
        before = 0

    else:
        before = num

    num = int(input())

    if num == 0:
        break

    if before < num:
        count += 1

print(count)
