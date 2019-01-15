'''
Statement
The first line contains the number of records. After that, each entry contains the name of the candidate and the number of votes they got in some state. Count the results of the elections: sum the number of votes for each candidate. Print candidates in the alphabetical order.

Example input
5
McCain 10
McCain 5
Obama 9
Obama 8
McCain 1

Example output
McCain 16
Obama 17
'''
import collections

n = int(input())
dic = {}

for _ in range(n):
    key, val = input().split()

    if key in dic.keys():
        dic[key] += int(val)

    else:
        dic[key] = int(val)

for key, val in sorted(dic.items(), key=lambda x: x[0]):
    print(key, val)
