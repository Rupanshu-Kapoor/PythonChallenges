"""
Majority Element:
https://leetcode.com/problems/majority-element/description/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == numslength
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""


class Solution:

    def majorityElementBF(self, nums: list[int]) -> int:
        """
        Brute force approach
        :TC: O(N*N)
        :SC: O(1)
        :param nums:
        :return:
        """
        for i in nums:
            # for every element in nums, count its occurrence
            count = 0
            for j in nums:
                if j == i:
                    count += 1
                # if occurrence are more than half the size of nums, that element is majority element
                if count > len(nums) // 2:
                    return i

    def majorityElementBT(self, nums: list[int]) -> int:
        """
        using Hashing
        :TC: O(N log N) + O(N)
        :SC: 0(N)
        :param nums:
        :return:
        """
        # hash_map to store the count of every element
        hash_map = {}
        for i in nums:
            # increase count of elements every time they appear
            hash_map[i] = hash_map.get(i, 0) + 1

        for i in hash_map:
            # loop through hash_map to find the majority occurring element
            if hash_map[i] > len(nums) // 2:
                return i

    def majorityElementOP(self, nums: list[int]) -> int:
        """
        Based on Moore's voting algorithm
        :TC: O(N) + O(N)
        :SC: O(1)
        :param nums:
        :return:
        """
        element = None
        count = 0
        for i in nums:
            if count == 0:
                element = i
            if i == element:
                count += 1
            else:
                count -= 1
        count = nums.count(element)
        if count > len(nums) // 2:
            return element


a = [2, 2, 1, 1, 1, 2, 21, 1, 1, 1, 1, 1, 1]

obj = Solution()
print(obj.majorityElementBT(a))
print(obj.majorityElementBF(a))
print(obj.majorityElementOP(a))
