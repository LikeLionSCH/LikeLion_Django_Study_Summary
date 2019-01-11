'''
Statement
Given a string, delete all the characters @ from this string.

Example input
Bilbo.Baggins@bagend.hobbiton.shire.me

Example output
Bilbo.Bagginsbagend.hobbiton.shire.me
'''
str = input()
print(str.replace('@', ''))
