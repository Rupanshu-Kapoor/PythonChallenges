"""
Palindrome Number
LeetCode: https://leetcode.com/problems/palindrome-number/description/
CodingNinja: https://www.codingninjas.com/studio/problems/palindrome-number_624662

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.

"""


def isPalindrome(num: int) -> bool:
    if num < 0:
        return False
    rev = 0
    temp = num
    while temp:
        last = temp % 10
        rev = (rev * 10) + last
        temp = temp // 10
    return rev == num


number = int(input("Enter a number to check palindrome: "))
print(isPalindrome(number))