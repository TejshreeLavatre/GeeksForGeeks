"""
Given an array C[], write a program that prints 1 if array is sorted in ascending order, else prints 0.

Input:
The first line of input contains an integer T denoting the number of test cases.
For each test case there will be two lines. First line contains the size of the array N.
Second line contains N space separated integers of the array C[i].

Output:
Print 1 if array is sorted, else print 0.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ C[i] ≤ 1200

Example:
Input
2
5
10 20 30 40 50
6
90 80 100 70 40 30

Output
1
0
"""


def isSortedArray(C):
    C = [int(x) for x in C.split()]
    valid = 0
    if N == 0 or N == 1:
        valid += 1
    for i in range(N-1):
        if C[i] <= C[i+1]:
            valid += 1
        else:
            return print("0")

    if valid != 0:
        return print("1")


T = int(input())
for _ in range(T):
    N = int(input())
    isSortedArray(str(input()))
