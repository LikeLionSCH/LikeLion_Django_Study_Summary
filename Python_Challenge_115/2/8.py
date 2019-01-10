'''
Statement
Given a year (as a positive integer), find the respective number of the century. Note that, for example, 20th century began with the year 1901.

Example input
2000

Example output
20
'''
import math
print(math.ceil(int(input()) / 100))
