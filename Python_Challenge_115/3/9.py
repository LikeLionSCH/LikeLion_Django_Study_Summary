'''
Statement
Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.

Example input #1
1
(January)

Example output #1
31

Example input #2
2
(February)

Example output #2
28
'''
month = int(input())

if month == 2:
    print(28)

elif month < 8:
    if month % 2 == 0:
        print(30)

    else:
        print(31)

else:
    if month % 2 == 0:
        print(31)

    else:
        print(30)
