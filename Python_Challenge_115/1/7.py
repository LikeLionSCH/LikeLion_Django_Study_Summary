'''
Statement
Given two timestamps of the same day: a number of hours, minutes and seconds for both of the timestamps. The moment of the first timestamp happened before the moment of the second one. Calculate how many seconds passed between them.

Example input #1
1
1
1
2
2
2

Example output #1
3661

Example input #2
1
2
30
1
3
20

Example output #2
50
'''
before_h = int(input())
before_m = int(input())
before_s = int(input())

after_h = int(input())
after_m = int(input())
after_s = int(input())

print(((after_h - before_h) * (60 ** 2))
      + (after_m - before_m) * 60
      + (after_s - before_s))
