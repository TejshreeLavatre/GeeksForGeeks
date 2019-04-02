"""
Print the table of a given number N.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow.
Each testcase contains one line of input denoting N.

Output:
For each testcase, print the table of N upto 10.

Constraints: 
1 <= T <= 100
1 <= N <= 1000

Example:
Input:
1
9 

Output:
9 18 27 36 45 54 63 72 81 90
"""


for _ in range(int(input())):
    N = int(input())
    output = ""
    for num in range(1, 11):
        output += "".join(str(N * num))
        output += "".join(" ")
    print(output)
