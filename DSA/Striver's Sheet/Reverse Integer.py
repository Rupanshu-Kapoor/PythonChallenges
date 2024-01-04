"""
7. Reverse Integer:https://leetcode.com/problems/reverse-integer/description/
Medium
Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:
"""


def revString(s: str) -> str:
    rev = ""
    for x in range(len(s) - 1, -1, -1):
        rev += s[x]
    return rev


def reverse(x: int) -> int:
    x = str(x)
    if x[0] == "-" or x[0] == "+":
        sign = x[0]
        temp = revString(x[1:])
        rev = sign + temp
    else:
        rev = revString(x)

    rev = int(rev)
    if not -pow(2, 31) <= rev <= pow(2, 31) - 1:
        rev = 0
    return rev


print(reverse(-1534236469))
# print(pow(2, 31) - 1)
