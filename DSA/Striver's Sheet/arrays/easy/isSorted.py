"""
1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution:
    def rightShift(self, nums: [int], shift_by: int):
        # 2 3 4 5 1
        # 1 2 3 4 5
        shifted_arr = nums[:]
        for i in range(shift_by):
            last = shifted_arr[-1]
            for j in range(len(shifted_arr) - 1, 0, -1):
                shifted_arr[j] = shifted_arr[j - 1]
            shifted_arr[0] = last
        return shifted_arr

    def check(self, nums: list[int]) -> bool:
        """
        brute force approach
        :param nums:
        :return:
        """

        for i in range(len(nums)):

            is_sorted = True
            shifted_arr = self.rightShift(nums, i)

            for j in range(1, len(shifted_arr)):
                if shifted_arr[j - 1] > shifted_arr[j]:
                    is_sorted = False
                    break
            if is_sorted:
                return True
        return is_sorted


obj = Solution()
# print(obj.check(nums=[3, 4, 5, 1, 2]))
ar = [1,2,3,4,5,6,7]
# ar = [-1, -100, 3 ,99]
print(obj.rightShift(ar,3))