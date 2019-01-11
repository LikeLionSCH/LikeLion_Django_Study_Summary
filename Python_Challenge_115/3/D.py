'''
Statement
Given a square of a chessboard. If it's a black square, print YES, otherwise print NO.

The program receives two integers from 1 to 8 specifying the column and row number of the square.

Example input #1
1
1

Example output #1
YES

Example input #2
1
2

Example output #2
NO
'''
x = int(input())
y = int(input())

if x % 2 != 0:
    if y % 2 != 0:
        print("YES")

    else:
        print("NO")

else:
    if y % 2 == 0:
        print("YES")

    else:
        print("NO")
