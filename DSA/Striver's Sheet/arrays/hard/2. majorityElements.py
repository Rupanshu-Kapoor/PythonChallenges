"""
Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
"""


class Solution:
    def majorityElementOP(self, v: list[int]) -> list[int]:
        count1 = count2 = 0
        ele1 = ele2 = None

        if len(v) == 1:
            return v
        for i in v:
            if count1 == 0 and i != ele2:
                count1 += 1
                ele1 = i
            elif count2 == 0 and i != ele1:
                count2 += 1
                ele2 = i
            elif i == ele1:
                count1 += 1
            elif i == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # ans =  sorted(ele1, ele2)
        ans = sorted([x for x in (ele1, ele2) if v.count(x) > len(v) // 3])
        return ans

    def majorityElementBF(self, nums: list[int]) -> list[int]:
        map = {}
        ans = []

        if len(nums) == 1:
            return nums

        for i in nums:
            map[i] = map.get(i, 0) + 1

        for i, j in map.items():
            if j > len(nums) // 3:
                ans.append(i)
        return ans


nums = [3,2,3]
obj = Solution()
print(obj.majorityElementBF(nums))
print(obj.majorityElementOP(nums))