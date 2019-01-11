'''
Statement
Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.

Example input #1
1
-2

Example output #1
-2

Example input #2
2
-1

Example output #2
no solution
'''
a = int(input())
b = int(input())

if a == 0:
    if b == 0:
        print("many solutions")

    else:
        print("no solution")

elif b / a == b // a:
    print(b // a)

else:
    print("no solution")
