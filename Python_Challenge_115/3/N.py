'''
Statement
Given integer coordinates of three vertices of a rectangle whose sides are parallel to coordinate axes, find the coordinates of the fourth vertex of the rectangle.

Example input #1
1
5
7
5
1
10
three vertices are (1, 5), (7, 5), (1, 10)

Example output #1
7
10

Example input #2
1
5
7
10
1
10

Example output #2
7
5
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

if x1 == x2:
    x4 = x3

elif x1 == x3:
    x4 = x2

elif x2 == x3:
    x4 = x1

if y1 == y2:
    y4 = y3

elif y1 == y3:
    y4 = y2

elif y2 == y3:
    y4 = y1

print(x4)
print(y4)
