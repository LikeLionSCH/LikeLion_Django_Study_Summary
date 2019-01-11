'''
Statement
Let's call an integer a palindrome if it remains the same after reading its digits from right to left. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.

Example input #1
1221

Example output #1
YES

Example input #2
1234

Example output #2
NO
'''
num = input()

if (num[0] == num[3]) and (num[1] == num[2]):
    print("YES")

else:
    print("NO") 
