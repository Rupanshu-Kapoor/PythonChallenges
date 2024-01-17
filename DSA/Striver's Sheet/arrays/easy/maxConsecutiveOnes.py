"""
85. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/description/
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = count = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0

        if count > max_count:
            max_count = count

        return max_count

obj = Solution()
arr = [1,1,0,1,1,1]
print(obj.findMaxConsecutiveOnes(arr))