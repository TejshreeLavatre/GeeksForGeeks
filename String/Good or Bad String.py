"""
In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'.
Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String
on the basis of following rules:

If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD".
A String is considered "GOOD" only if it is not “BAD”.

NOTE: String is considered as "BAD" if the above condition is satisfied even once. Else it is "GOOD"
and the task is to make the string "BAD".

Input:
The first line consists of an integer T i.e number of test cases. T testcases follow. The first and only line
of each test case consists of a string S.

Output:
For each testcase, in a new line, print "1"  if string is GOOD, else print "0".

Constraints:
1 <= T <= 100
1 <= |S| <= 100

Example:
Input:
2
aeioup??
bcdaeiou??
Output:
1
0

"""

def is_good_or_bad(S):
    vowel_count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    consonant = ''
    consonant_count = 0
    for i in S:
        if vowel_count > 5 or consonant_count > 3:
            break
        elif i in vowel:
            vowel_count += 1
            consonant_count = 0
        elif i == '?':
            vowel_count += 1
            consonant_count += 1
        else:
            consonant_count += 1
            vowel_count = 0
    if vowel_count > 5 or consonant_count > 3:
        print("0")
    else:
        print("1")

for _ in range(int(input())):
    S = input()
    is_good_or_bad(S)