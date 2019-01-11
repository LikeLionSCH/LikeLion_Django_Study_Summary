'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. Determine the length of the sequence. The sequence ends with 0. Print the length of the sequence (not counting the 0). The numbers following the number 0 should be omitted.

Example input
1
7
9
0
5

Example output
3
'''
count = 0

while int(input()) != 0:
    count += 1

print(count)
