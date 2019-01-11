'''
Statement
Given a string consisting of exactly two words separated by a space. Print a new string with the first and second words swapped: the second word is printed first. Consider all adjacent non-space characters a single word.

Can you solve it without using if-else and loops?

Example input
Hello, world!

Example output
world! Hello,
'''
str = input()
print(str.split()[1] + " " + str.split()[0])
