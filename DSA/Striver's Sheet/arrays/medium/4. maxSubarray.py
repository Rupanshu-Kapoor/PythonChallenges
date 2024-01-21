"""
Maximum Subarray:
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArrayBF(self, nums: list[int]) -> int:
        """
        Brute force: finds all the subarray in the given array and calculates their sum
                    the subarray with the maximum sum is our desired subarray
        :TC: O(n*n)
        :SC: O(1)
        :param nums:
        :return:
        """
        size = len(nums)
        total = -float("inf")
        if size < 2:
            return nums[0]
        for i in range(size):
            temp = 0
            for j in range(i,size):
                temp += nums[j]

                if temp > total:
                    total = temp
        if temp > total:
            total = temp
        return total


    def maxSubArrayOP(self, nums: list[int]) -> int:
        """
        Kadane's Algo: calculates max sum of a subarray, but if all the elements are -ve then returns 0

                if at any point the sum of array goes below zero, then subarray before that point
                cannot give maximum sum, as -ve value will reduce the total sum.
                so take the after than point do following steps:
                1. current_sum = current_sum + ith index
                2. max_sum = max(current_sum, max_sum)
                3. if current_sum < 0 : current_sum = 0 (forget the subarray before this)
        :TC: O(N)
        :SC: O(1)
        :param nums:
        :return:
        """

        cur_sum = 0
        max_sum = float("-inf")
        for value in nums:
            # add value to the cur_some to find the current sum
            cur_sum += value
            # update max_sum if cur_sum exceeds max_sum
            max_sum = max(max_sum, cur_sum)
            # if cur_sum is negative, then make cur_sum zero
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

a = [-10,-2,-1]
print(Solution().maxSubArrayBF(a))
print(Solution().maxSubArrayOP(a))


