'''
Statement
The text is given in a single line. For each word of the text count the number of its occurrences before it.

Example input
one two one two three two four three

Example output
0 0 1 1 0 2 0 1
'''
num_dic = {}
arr = input().split()

for val in arr:
    if val in num_dic.keys():
        num_dic[val] += 1
        print(num_dic[val], end=" ")

    else:
        num_dic[val] = 0
        print(num_dic[val], end=" ")
