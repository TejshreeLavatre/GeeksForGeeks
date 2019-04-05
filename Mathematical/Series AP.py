"""
Given the first 2 terms A and B of an Arithmetic Series, tell the Nth term of the series.

Input:
The first line of input contains an integer, the number of test cases T.
T testcases follow. Each testcase in its first line should contain two positive integer A and B(First 2 terms of AP).
In the second line of every testcase it contains of an integer N.

Output:
For each testcase, in a new line, print the Nth term of the Arithmetic Progression.

Constraints:
1 <= T <= 100
-103 <= A <= 103
-103 <= B <= 103
1 <= N <= 104

Example:
Input:
2       Number of Test cases
2 3     A, B
4       N
1 2     A, B
10      N

Output:
5
10
"""

T = int(input())                         # Number of test cases
for _ in range(T):
    A, B = map(int, input().split())
    N = int(input())
    D = B - A                           # Difference
    print(A+(N-1)*D)
