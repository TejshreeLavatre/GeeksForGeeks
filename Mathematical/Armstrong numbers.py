"""
For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of
three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.
For example, 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow.
Each test case contains a positive integer N.

Output:
For each testcase, in a new line, print "Yes" if it is a armstrong number else print "No".

Constraints:
1 <= T <= 31
100 <= N < 1000

Example:
Input:
1
371
Output:
Yes
"""

for _ in range(int(input())):
    N = int(input())
    num_list = [int(num) for num in str(N)]
    i = 0
    if (num_list[i] ** 3) + (num_list[i + 1] ** 3) + (num_list[i + 2] ** 3) == N:
        print("Yes")
    else:
        print("No")
