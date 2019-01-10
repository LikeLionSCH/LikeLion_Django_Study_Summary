'''
Statement
N students take K apples and distribute them among each other evenly. The remaining (the indivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?

The program reads the numbers N and K. It should print the two answers for the questions above.

Example input
6
50

Example output
8
2
'''
std = int(input())
apple = int(input())

print(apple // std)
print(apple % std)
