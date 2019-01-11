'''
Statement
Chess knight can move to a square that is two squares away horizontally and one square vertically, or two squares vertically and one square horizontally. The complete move therefore looks like the letter L. Given two different squares of the chessboard, determine whether a knight can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a knight can go from the first square to the second one in a single move or NO otherwise.

Example input
2
4
3
2

Example output
YES
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x2 - x1) == 2:
    if abs(y2 - y1) == 1:
        print("YES")

    else:
        print("NO")

elif abs(y2 - y1) == 2:
    if abs(x2 - x1) == 1:
        print("YES")

    else:
        print("NO")

else:
    print("NO")
