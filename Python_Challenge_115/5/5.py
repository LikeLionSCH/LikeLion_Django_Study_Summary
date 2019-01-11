'''
Statement
Given a string that may contain a letter f. Print the index of the first and last occurrence of f. If the letter f occurs only once, then output its index once. If the letter f does not occur, print -1.

Example input #1
comfort

Example output #1
3

Example input #2
office

Example output #2
1 2

Example input #3
hello

Example output #3
-1
'''
str = input()
first, last = len(str) - 1, 0

if 'f' in str:
    for i in range(len(str)):
        if str[i] == 'f':
            if first > i:
                first = i

            if last < i:
                last = i

    print(first, last) if first != last else print(first)

else:
    print(-1)
