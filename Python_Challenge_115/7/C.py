'''
Statement
It is possible to place 8 queens on an 8×8 chessboard so that no two queens threaten each other. Thus, it requires that no two queens share the same row, column, or diagonal.

Given a placement of 8 queens on the chessboard. If there is a pair of queens that violates this rule, print YES, otherwise print NO. The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chessboard with rows and columns numbered from 1 to 8.

Example input
1 5
2 3
3 1
4 7
5 2
6 8
7 6
8 4
(shown on the picture)

Example output
NO
'''
eight_quuen = []
check = False

for _ in range(8):
    eight_quuen.append(list(map(int, input().split())))

for i in eight_quuen:
    if check:
        break

    for j in eight_quuen:
        if i == j:
            continue

        else:
            if i[0] == j[0] or i[1] == j[1]:
                check = True
                break

            else:
                if i[0] != j[0] and i[1] != j[0]:
                    if abs(i[0] - j[0]) == abs(i[1] - j[1]):
                        check = True
                        break

print("No") if not check else print("Yes")
