"""
Write a program to check if the sum of digits of a given number N is a palindrome number or not.

Input:
The first line of the input contains T denoting the number of testcases. T testcases follow.
Then each of the T lines contains single positive integer N denoting the value of number.

Output:
For each testcase, in a new line, output "YES" if palindrome else "NO". (without the quotes)

Constraints:
1 <= T <= 200
1 <= N <= 1000

Example:
Input:
2
56
98
Output:
YES (5+6 = 11. Palindrome)
NO  (9+8 = 17. Not a Palindrome)
"""


def sum_of_digits(N):
    addition = 0
    while N:
        addition += N % 10
        N //= 10
    return addition


def isPalindrome(N):
    temp = N
    reverse = 0
    while temp:
        reverse = (reverse*10) + temp % 10
        temp //= 10
    return N == reverse


for _ in range(int(input())):
    N = int(input())
    N = sum_of_digits(N)
    print("YES" if isPalindrome(N) else "NO")
