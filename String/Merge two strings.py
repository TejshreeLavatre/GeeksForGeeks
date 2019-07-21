"""
Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1
then the first character of S2 and so on till the strings end.

NOTE: Add the whole string if other string is empty.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case contains two strings S1 and S2.

Output:
For each test case, in a new line, print the merged string.

Constraints:
1 <= T <= 100
1 <= |S1|, |S2| <= 104

Example:
Input:
2
Hello Bye
abc def

Output:
HBeylelo
adbecf

"""


def isMerge(S1, S2):
    answer = ""
    if len(S1) > len(S2):
        smaller = len(S2)
        larger = len(S1)
        remainder = S1[smaller:larger]
    else:
        smaller = len(S1)
        larger = len(S2)
        remainder = S2[smaller:larger]
    for i in range(smaller):
        answer += S1[i] + S2[i]
    answer += remainder
    print(answer)


for _ in range(int(input())):
    S1, S2 = map(str, input().split(" "))
    isMerge(S1, S2)
