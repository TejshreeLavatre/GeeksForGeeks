"""
Given a string S, Check if characters of the given string can be rearranged to form a palindrome.
For example characters of “geeksogeeks” can be rearranged to form a palindrome “geeksoskeeg”,
but characters of “geeksforgeeks” cannot be rearranged to form a palindrome.

Input:
First line consists of integer T  denoting the number of test cases. T testcases follow.
For each testcase there are one line of input containing string S.

Output:
For each testcase, in a new line, print "Yes" if is possible to make it a palindrome, else "No".

Constraints:
1 <= T <= 100
1 <= |S| <= 1000

Example:
Input:
2
geeksogeeks
geeksforgeeks
Output:
Yes
No
"""


from collections import defaultdict


def palindrome(S):
    oddCount = 0
    d = defaultdict(int)     # Creates a dictionary with alphabets as key and num of occurrence as value
    for i in S:
        d[i] += 1
        if d[i] % 2 == 1:
            oddCount += 1
        else:
            oddCount -= 1
    return oddCount <= 1


for _ in range(int(input())):
    if palindrome(input()):
        print("Yes")
    else:
        print("No")
