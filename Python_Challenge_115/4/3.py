'''
Statement
10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.

Example input
0
1
2
3
4
5
6
7
8
9

Example output
45
'''
sum = 0

for _ in range(10):
    sum += int(input())

print(sum)
