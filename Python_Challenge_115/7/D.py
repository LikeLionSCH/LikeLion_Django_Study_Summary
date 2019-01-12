'''
Statement
In bowling, the player starts with 10 pins in a row at the far end of a lane. The goal is to knock all the pins down. For this assignment, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled.

The balls are numbered from 1 to N for this situation. The subsequent number pairs, one for each K represent the first and last (inclusive) positions of the pins that were knocked down with each roll. Print a sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked down.

Example input
10 3
8 10
2 5
3 6

Example output
I.....I...
'''
K, N = map(int, input().split())
pin = ['I'] * K

for _ in range(N):
    pairs = list(map(int, input().split()))

    for i in range(pairs[0] - 1, pairs[1]):
        pin[i] = '.'

print(''.join(pin))
