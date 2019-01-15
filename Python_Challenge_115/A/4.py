'''
Statement
Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.

Example input
2
apple orange banana
banana orange

Example output
banana
'''
dic = {}
max = 0

for _ in range(int(input())):
    arr = input().split()

    for key in arr:
        if key in dic.keys():
            dic[key] += 1

            if dic[key] > max:
                max = dic[key]

        else:
            dic[key] = 1

            if dic[key] > max:
                max = dic[key]

for (key, val) in sorted(dic.items(), key=lambda x: x[0]):
    if val == max:
        print(key)
        break
