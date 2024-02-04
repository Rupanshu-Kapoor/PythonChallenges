"""
Rearrange Array Elements by Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
Medium

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should rearrange the elements of nums such that the modified array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].


Constraints:
2 <= nums.length <= 2 * 105
nums.length is even
1 <= |nums[i]| <= 105
nums consists of equal number of positive and negative integers.
"""


class Solution:
    def rearrangeArrayBF(self, nums: list[int]) -> list[int]:
        """
        brute force: 1. we take 2 empty array of size n/2, for storing positive and negative numbers
                    2. we store positive numbers in p_arr and negative numbers in n_arr
                    3. Then we loop till n/2 and place postive at even indexes and negative at odd indexes
        :param nums:
        :return:
        """
        p_arr = []
        n_arr = []

        for i in nums:
            if i < 0:
                n_arr.append(i)
            else:
                p_arr.append(i)

        for i in range(len(nums) // 2):
            nums[2 * i] = p_arr[i]
            nums[2 * i + 1] = n_arr[i]

        return nums

    def rearrangeArrayOP(self, nums: list[int]) -> list[int]:
        pos_ind = 0
        neg_ind = 1
        ans = [0] * len(nums)

        for i in nums:
            if i > 0:
                ans[pos_ind] = i
                pos_ind += 2
            else:
                ans[neg_ind] = i
                neg_ind += 2

        return ans


nums = [3, 1, -2, -5, 2, -4]
obj = Solution()
print(nums)
print(obj.rearrangeArrayBF(nums))
# print(nums)
