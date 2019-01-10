'''
Statement
A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

Example input
10
15
2

Example output
20 30
'''
A = int(input())
B = int(input())
N = int(input())
dollars, cents = A * N, B * N
print(dollars + (cents // 100), cents % 100)
