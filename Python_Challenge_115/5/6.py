'''
Statement
Given a string that may contain a letter p. Print the index of the second occurrence of p. If the letter p occurs only once, then print -1, and if the string does not contain the letter p, then print -2.

Example input #1
appropriate

Example output #1
2

Example input #2
spare

Example output #2
-1

Example input #3
reason

Example output #3
-2
'''
str = input()

if 'p' not in str:
    print(-2)

else:
    if str.count('p') == 1:
        print(-1)

    else:
        check = False

        for i in range(len(str)):
            if str[i] is 'p':
                if not check:
                    check = True

                else:
                    print(i)
                    break
