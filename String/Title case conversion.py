"""
Given a string S, write a program to title case every first letter of words in string.

Input:
The first line consists of an integer T i.e number of test cases. T testcases follow.
The first and only line of each test case consists of a string S.

Output:
For each testcase, in a new line, print the required output.

Constraints:
1 <= T <= 100
1 <= |S| <= 1000

Example:
Input:
1
I love programming
Output:
I Love Programming
"""

for _ in range(int(input())):
    S = str(input())
    print(S.title())


"""
Alternative solution

for _ in range(int(input())):
    S = str(input())
    print(" ".join(word.capitalize() for word in S.split()))
"""