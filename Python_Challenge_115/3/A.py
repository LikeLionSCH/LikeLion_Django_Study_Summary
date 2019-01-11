'''
Statement
Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).

Example input
10
5
10

Example output
2
'''
num1 = input()
num2 = input()
num3 = input()

if num1 == num2:
    if num2 == num3:
        print(3)

    else:
        print(2)

elif num2 == num3 or num1 == num3:
    print(2)

else:
    print(0)
