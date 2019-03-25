"""
Given a string S, check if it is palindrome or not.

Input:
The first line contains 'T' denoting the number of test cases. T testcases follow. Each testcase contains
two lines of input. The first line contains the length of the string and the second line contains the string S.

Output:
For each testcase, in a new line, print "Yes" if it is a palindrome else "No". (Without the double quotes)

Constraints:
1 <= T <= 30
1 <= N <= 100

Example:
Input:
1
4
abba
Output:
Yes
"""

def isPalindrome(S):
    for _ in S:
        if S == S[::-1]:
            print("Yes")
            break
        else:
            print("No")
            break


for _ in range(int(input())):
    len = int(input())
    S = str(input())
    isPalindrome(S)


