'''
Statement
A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

Example input
700
750

Example output
2
'''
import math
N = int(input())
M = int(input())
print(math.ceil(M / N))
