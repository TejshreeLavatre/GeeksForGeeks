"""
Given two strings a and b consisting of lowercase characters. The task is to check whether
two given strings are anagram of each other or not. An anagram of a string is another string
that contains same characters, only the order of characters can be different.
For example, “act” and “tac” are anagram of each other.

Input:
The first line of input contains an integer T denoting the number of test cases.
Each test case consist of two strings in 'lowercase' only, in a single line.

Output:
Print "YES" without quotes if the two strings are anagram else print "NO".

Constraints:
1 ≤ T ≤ 30
1 ≤ |s| ≤ 10^16

Example:
Input:
2
geeksforgeeks forgeeksgeeks
allergy allergic

Output:
YES
NO

Explanation:
Testcase 1: Both the string have same characters with same frequency. So, both are anagrams.
Testcase 2: Characters in both the strings are not same, so they are not anagrams.
"""


from collections import Counter

def ifAnagram(S):
    S1, S2 = map(str, S.split(" "))
    if len(S1) != len(S2):
        return print("NO")
    elif Counter(S1) == Counter(S2):
        return print("YES")
    else:
        return print("NO")


for _ in range(int(input())):
    S = str(input())
    ifAnagram(S)







