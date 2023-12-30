'''

1897. Redistribute Characters to Make All Strings Equal:
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/?envType=daily-question&envId=2023-12-30

You are given an array of strings words (0-indexed).
In one operation, pick two distinct indices i and j, where words[i] is a non-empty string,
 and move any character from words[i] to any position in words[j].
Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''


class Solution(object):
    def makeEqual(self, words):
        if len(words) == 1:
            return True

        total_char_count = sum(len(s) for s in words)

        if total_char_count % len(words) != 0:
            return False

        my_map = [0] * 26
        for s in words:
            for c in s:
                my_map[ord(c) - ord('a')] += 1

        for i in my_map:
            if i % len(words) != 0:
                return False

        return True


obj = Solution()
words = ["abc","aabc","bc"]
print(obj.makeEqual(words))