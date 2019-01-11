'''
Statement
Chess rook moves horizontally or vertically. Given two different squares of the chessboard, determine whether a rook can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a rook can go from the first square to the second one in a single move or NO otherwise.

Example input
4
4
5
5

Example output
NO
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 - x1 == 0 or y2 - y1 == 0:
    print("YES")

else:
    print("NO")
