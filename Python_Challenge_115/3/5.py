'''
Statement
Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.

Example input #1
-5
10

Example output #1
YES

Example input #2
5
10

Example output #2
NO
'''
num1 = int(input())
num2 = int(input())

if (num1 > 0 and num2 < 0) \
    or (num1 < 0 and num2 > 0):
    print("YES")

else:
    print("NO")
