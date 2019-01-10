'''
Statement
The hour hand of an analog clock turned α degrees since the midnight. Determine the angle by which the minute hand turned since the start of the current hour. Input and output in this problems are integers.

Example input
190
(6:20)

Example output
120
(20 min)
'''
a = int(input())
hour = a // 30
remain_angle = a - (hour * 30)
ratio = remain_angle / 30
print(int(12 * ratio * 30))
