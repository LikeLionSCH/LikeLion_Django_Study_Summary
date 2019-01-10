'''
Statement
Write a program that reads an integer number and prints its previous and next numbers. See the example below.

Example input
179

Example output
The next number for the number 179 is 180
The previous number for the number 179 is 178
'''
num = int(input())
print("The next number for the number "
      + str(num) + " is " + str(num + 1))
print("The previous number for the number "
      + str(num) + " is " + str(num - 1))
