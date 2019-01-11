'''
Statement
For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.

To do that, you can use the sep and end arguments for the function print().

Example input
3

Example output
1
12
123
'''
N = int(input())
output = ""

for i in range(1, N + 1):
    output += str(i)
    print(output)
