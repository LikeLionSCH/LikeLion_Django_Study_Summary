'''
Statement
For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.

Try to use the cascade if-elif-else for it.

Example input
179

Example output
1
'''
X = int(input())

if X > 0:
    print(1)

elif X == 0:
    print(0)

else:
    print(-1)
