'''
Statement
For the given integer N calculate the following sum:

1³ + 2³ + ... + N³

Example input
3

Example output
36
'''
N = int(input())
sum = 0

for i in range(1, N + 1):
    sum += i ** 3

print(sum)
