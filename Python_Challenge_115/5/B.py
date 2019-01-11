'''
Statement
Given a string in which the letter h occurs at least twice, replace every occurrence of the letter h by the letter H, except for the first and the last ones.

Example input
In the hole in the ground there lived a hobbit

Example output
In the Hole in tHe ground tHere lived a hobbit
'''
str = input()
result = ""

for idx, val in enumerate(str.split('h')):
    if idx == 0:
        result += (val + 'h')

    elif idx == 1:
        result += val

    elif idx == len(str.split('h')) - 1:
        result += ('h' + val)

    else:
        result += ('H' + val)

print(result)
