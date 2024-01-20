"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def twoSumBF(self, nums: list[int], target: int) -> list[int]:
        """
        brute force approach: take an element(ith) and check its sum with every other element(jth)
            if matches return the index of those 2 elements otherwise take (i+1th) element and
            repeat the same
        :TC: O(n*n)
        :SC: O(1)
        :param nums: array
        :param target: target value
        :return: 2 indexes whose sum matches to target
        """
        size = len(nums)
        # loop all the elements
        for i in range(size):
            # to check every other element after ith element if its sum with ith element = target
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumBT(self, nums: list[int], target: int) -> list[int]:
        """
        better solution: take a element(i) and calculate how much it need to make sum = target (say rem)
            now find that rem in hash_map, if found return the index of those elements
            if not store the 'i' as key and its index as value
        :TC: O(n logn)
        :SC: O(n)
        :param nums:
        :param target:
        :return:
        """
        hash_map = {}  # key = value, value = ind
        for ind, value in enumerate(nums):
            rem = target - value  # to find if the required elements is already present in hash_map
            if rem in hash_map:
                ind2 = hash_map[rem]  # if found, get the index
                return [ind2, ind]
                # index of ind2 < ind because ind2 has been already iterated and stored in the hash_map
            hash_map[value] = ind

    def twoSumBT2(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = 1
        nums.sort()
        while i < len(nums) and j < (len(nums)):

            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

            elif nums[i] + nums[j] < target:
                i += 1
                j += 1
            elif nums[i] + nums[j] > target:
                i -= 1


a = [3,2,3]
t = 6
obj = Solution()
print(obj.twoSumBF(a, t))
print(obj.twoSumBT(a, t))
print(obj.twoSumBT2(a, t))
