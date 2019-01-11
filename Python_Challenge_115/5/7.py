'''
Statement
Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.

Example input
In the hole in the ground there lived a hobbit

Example output
In tobbit
'''
str = input()
first, last = len(str) - 1, 0

for i in range(len(str)):
    if str[i] is 'h':
        if first > i:
            first = i

        if last < i:
            last = i

print(str[:first] + str[last + 1:])
