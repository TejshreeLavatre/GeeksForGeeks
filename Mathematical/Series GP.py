"""
Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow.
Each test case in its first line contains two positive integer A and B (First 2 terms of GP).
In the second line of every test case it contains of an integer N.

Output:
In each separate line print the Nth term of the Geometric Progression. Print the floor ( floor(2.3)=2 ) of the answer.

Constraints:
1 <= T <= 30
-100 <= A <= 100
-100 <= B <= 100
1 <= N <= 5

Example:
Input:
2
2 3
1
1 2
2

Output:
2
2

Explanation:
Testcase 2: The second term of series whose common ratio is 2 will be 2.
"""

import math
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    N = int(input())
    R = B / A                               # ratio = (n+1)th term / (n)th term
    nth_term = A * (R ** (N - 1))           # nth term of GP given by An = A(R^(N-1))
    print(math.floor(nth_term))
