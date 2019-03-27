"""
Calculate the angle between hour hand and minute hand.
There can be two angles between hands, we need to print minimum of two. Also, we need to
print floor of final result angle. For example, if the final angle is 10.61, we need to print 10.

Input:
The first line of input contains a single integer T denoting the number of test cases.
Then T test cases follow. Each test case consists of one line containing two space separated
numbers h and m where h is hour and m is minute.

Output:
Corresponding to each test case, print the angle b/w hour and min hand in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ h ≤ 12
1 ≤ m ≤ 60

Example:
Input
2
9 60
3 30

Output
90
75
"""

from math import floor


def calcAngle(h, m):
    if h == 12:
        h = 0
    if m == 60:
        m = 0

    hourAngle = (h * 60 + m) * 0.5          #Convert hr to mins. 0.5 degree shift of hr hand for every min
    minuteAngle = m * 6                     # 6 degree shift of minute hand for every minute
    angle = abs(hourAngle - minuteAngle)
    angle = min(360 - angle, angle)         # Returns smaller value of angle
    return print(floor(angle))


for _ in range(int(input())):
    h, m = map(float, input().split())      # float is used since input can be in decimal values
    calcAngle(h, m)
