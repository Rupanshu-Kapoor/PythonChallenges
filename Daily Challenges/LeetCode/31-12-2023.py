"""
1624. Largest Substring Between Two Equal Characters:https://leetcode.com/problems/
    largest-substring-between-two-equal-characters/?envType=daily-question&envId=2024-01-03
Easy
Topics
Companies
Hint
Given a string s, return the length of the longest substring between two equal characters,
excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.


Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
"""


def maxLengthBetweenEqualCharacters(string):
    result = -1

    for i in range(len(string)):

        # index = [x for x in range(len(string)) if string[x] == string[i]]
        index = [ind for ind, char in enumerate(string) if char == string[i]]
        if index:
            index = max(index)
        if index - 1 - i > result:
            result = index - 1 - i
        index = 0
    return result


print(maxLengthBetweenEqualCharacters("aa"))
