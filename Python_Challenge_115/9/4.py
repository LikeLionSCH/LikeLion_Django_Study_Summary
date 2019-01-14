'''
Statement
Given a sequence of numbers, scan them from left to right and for each number print YES if this number was already seen or NO if it appears for the first time.

Example input
1 2 3 2 3 4

Example output
NO
NO
NO
YES
YES
NO
'''
arr = input().split()
seted_arr = set(arr)

for i in arr[:]:
    if i in seted_arr:
        seted_arr.remove(i)
        print('No')

    else:
        print('Yes')
