"""
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

 Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pass
        count = 0
        for i,val in enumerate(nums):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
                # if sum > k:
                #     break
        return count


a = [3,-3,1,1,1]
b = 3
obj = Solution()
print(obj.subarraySum(a,b))

