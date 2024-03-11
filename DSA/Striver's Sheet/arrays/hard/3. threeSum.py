"""
3Sum:https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from testing import stressTest


class Solution:
    def threeSumBT(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        for i in range(len(nums)):
            map = {}
            for j in range(i + 1, len(nums)):
                search = -(nums[i] + nums[j])
                if search in map:
                    temp = sorted([nums[i], nums[j], search])
                    ans.add(tuple(temp))
                map[nums[j]] = 1
                # ans.append(temp)
        ans = [list(t) for t in ans]
        return ans

    def threeSumOP(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k != len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        # ans = [list(x) for x in ans]
        return ans


nums = [[-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2], [2, 1, 1, 3, 1, 4, 5, 6], [-1, 0, 1, 2, -1, -4]]
obj = Solution()

for i in nums:
    print(stressTest.stressTest().testResult(obj.threeSumOP(i), obj.threeSumBT(i)))
#
print(obj.threeSumBT(nums[-1]))
print(obj.threeSumOP(nums[-1]))
