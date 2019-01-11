'''
Statement
Given a string, delete all its characters whose indices are divisible by 3.

Example input
Python

Example output
yton

'''
str = input()

for i in range(len(str)):
    if i % 3 != 0:
        print(str[i], end='')
print()
