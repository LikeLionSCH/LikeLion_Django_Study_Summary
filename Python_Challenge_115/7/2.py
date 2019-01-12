'''
Statement
Given a list of numbers, print all its even elements. Use a for-loop that iterates over the list itself and not over its indices. That is, don't use range()

Example input
1 2 2 3 3 3 4

Example output
2 2 4
'''
print(' '.join([val for val in input().split() if int(val) % 2 == 0]))
