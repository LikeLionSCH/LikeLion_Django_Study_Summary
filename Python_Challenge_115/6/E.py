'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Determine the length of the widest fragment where all the elements are equal to each other.

Example input
1
7
7
9
1
0

Example output
2
'''
import itertools

a = []

while True:
    num = int(input())

    if num == 0:
        break

    a.append(num)

z = [(x[0], len(list(x[1]))) for x in itertools.groupby(a)]
print(max(z, key=lambda x: x[1])[1])
