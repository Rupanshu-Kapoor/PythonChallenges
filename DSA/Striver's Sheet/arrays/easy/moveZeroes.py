"""
Move Zeroes: https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?

"""


class Solution:

    def moveZeroes(self, nums: list[int]) -> None:
        """
        brute force approach
        :TC: O(n) + O(x) + O(n-x) = O(2n)
        :param nums:
        :return:
        """
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])

        for i in range(len(temp)):
            nums[i] = temp[i]

        for i in range(len(temp), len(nums)):
            nums[i] = 0

    def moveZeroes2(self, nums: list[int]) -> None:
        """
        Optimal approach
        :TC: = O(n)
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        j = -1
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
            # else:
            #     count += 1
        # nums[j+1:] = [0] * count


arr = [0,1,0,2,3,4,0]
print(arr)
obj = Solution()
obj.moveZeroes(arr)
print(arr)
