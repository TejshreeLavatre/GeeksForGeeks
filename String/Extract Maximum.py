"""
You have been given an alphanumeric string S, extract maximum numeric value from that string.
Alphabets will only be in lower case.

Input:
The first line contains a single integer T i.e. the number of test cases. T testcases follow.
The first and only line consists of a String S.

Output:
For each testcase, in a new line, print the Maximum number extracted from the string S.

Constraints:
1 <= T <= 100
2 <= |S| <= 200

Example:
Input:
3
100klh564abc365bg
abvhd9sdnkjdfs
abchsd0sdhs
Output:
564
9
0

Explanation:
Test Case 1: The maximum number found in the string is "564".


"""

for _ in range(int(input())):
    S = input()
    maxnum = temp = 0
    for i in S:
        if i.isdigit():
            temp = temp*10 + int(i)
            if temp > maxnum:
                maxnum = temp
        else:
            temp = 0
    print(maxnum)