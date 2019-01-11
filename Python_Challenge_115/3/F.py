'''
Statement
Chess king moves one square in any direction. Given two different squares of the chessboard, determine whether a king can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a king can go from the first square to the second one in a single move or NO otherwise.

Example input
4
4
5
5

Example output
YES
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x2 - x1) > 1 or abs(y2 - y1) > 1:
    print("NO")

else:
    print("YES")
