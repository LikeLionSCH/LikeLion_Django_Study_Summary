'''
Statement
Given a sequence of distinct non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.

Example input
1
7
9
0

Example output
7
'''
first, second, check = 0, 0, True

while True:
    num = int(input())

    if num == 0:
        break

    if check:
        first = num
        check = False

    else:
        if first < num:
            first, second = num, first

        else:
            if second < num:
                second = num

print(second)
