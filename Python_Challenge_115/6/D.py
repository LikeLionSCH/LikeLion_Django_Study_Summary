'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Find how many elements of this sequence are equal to its largest element.

Example input #1
1
7
9
0

Example output #1
1

Example input #2
1
3
3
1
0

Example output #2
2

'''
max, count = -1, 0

while True:
    num = int(input())

    if num == 0:
        break

    if count == 0:
        max, count = num, count + 1

    else:
        if max < num:
            max, count = num, 1

        elif max == num:
            count += 1

print(count)
