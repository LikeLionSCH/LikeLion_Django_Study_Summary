'''
Statement
Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) in the year 2017, print the month and the day of the next day to it.

Example input #1
3
30
(March 30)

Example output #1
3
31

Example input #2
3
31
(March 31)

Example output #2
4
1
'''
month = int(input())
day = int(input())

if month == 2:
    if day == 28:
        print(month + 1)
        print(1)

    else:
        print(month)
        print(day + 1)

elif month < 8:
    if month % 2 == 0:
        if day == 30:
            print(month + 1)
            print(1)

        else:
            print(month)
            print(day + 1)

    else:
        if day == 31:
            print(month + 1)
            print(1)

        else:
            print(month)
            print(day + 1)

else:
    if month % 2 == 0:
        if day == 31:
            if month == 12:
                print(1)
                print(1)

            else:
                print(month + 1)
                print(1)

        else:
            print(month)
            print(day + 1)

    else:
        if day == 30:
            print(month + 1)
            print(1)

        else:
            print(month)
            print(day + 1)
