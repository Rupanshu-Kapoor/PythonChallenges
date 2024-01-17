"""
Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-17
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        map = {}
        is_unique = True
        for i in arr:
            map[i] = map.get(i, 0) + 1

        values = map.values()
        for key, value in map.items():
            for k,v in map.items():
                if key!= k and value == v:
                    return False
        return is_unique



arr = [1,2,2,1,1,3]
obj = Solution()
print(obj.uniqueOccurrences(arr))