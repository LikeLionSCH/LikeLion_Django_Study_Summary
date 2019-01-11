'''
Statement
Given a string in which the letter h occurs at least twice, reverse the sequence of characters enclosed between the first and last occurrences of it.

Example input
In the hole in the ground there lived a hobbit

Example output
In th a devil ereht dnuorg eht ni eloh ehobbit
'''
str = input()
first, last = len(str) - 1, 0

for i in range(len(str)):
    if str[i] is 'h':
        if first > i:
            first = i

        if last < i:
            last = i

start = str[:first + 1]
finish = str[last:]
mid = ""

for i in range(1, (last - first) // 2 + 1):
    if i != (last - first) // 2:
        start += str[last - i]

    mid += str[first + i]

print(start + mid[::-1] + finish)
