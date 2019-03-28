"""
Write a program that calculates the day of the week for any particular date in the past or future.

Input:
The first line of input contains a single integer T denoting the number of test cases.
Then T test cases follow. Each test case consist of one line. The first line of each test case
consists of an integer d,m and y, d is day, m is month and y is the year.

Output:
Print day of given date.

Constraints:
1 ≤ T ≤ 100
1990 ≤ Y ≤ 2100

Example:
Input:
2
28 12 1995
30 8 2010

Output
Thursday
Monday
"""

import calendar
import datetime


def dayOfWeek(D):
    Day = datetime.datetime.strptime(D, '%d %m %Y').weekday()
    return calendar.day_name[Day]


for _ in range(int(input())):
    print(dayOfWeek(str(input())))
