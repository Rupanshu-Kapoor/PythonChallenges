"""
Leetcode: 1464. Maximum Product of Two Elements in an Array
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value,
that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12


Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

"""

import random
class Solution:

    def randomArrayGenerator(self, numbers: int, rand_range: int) -> list[int]:
        random_array = []
        for i in range(numbers):
            rand_number = random.randrange(1,rand_range)
            random_array.append(rand_number)
        return random_array

    def maxProductSorting(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)

    def maxProductSearching(self, nums:list[int]) -> int:
        if len(nums) < 1:
            return -1
        if len(nums) == 2:
            return (nums[0]-1) * (nums[1]-1)
        else:
            max1 = 0
            max2 = 0

            for i in range(len(nums)):
                if nums[i] > max1:
                    max1 = nums[i]
                    maxInd = i
            for j in range(len(nums)):
                if nums[j] > max2 and j != maxInd:
                    max2 = nums[j]
            return (max1-1) * (max2-1)

    def maxProductSearching2(self, nums:list[int]) -> int:
        if len(nums) < 1:
            return -1
        if len(nums) == 2:
            return (nums[0]-1) * (nums[1]-1)
        else:
            max1 = max2 = 0
            for num in nums:
                if num > max1:
                    max2 = max1
                    max1 = num
                elif num > max2:
                    max2 = num
            return (max1-1)*(max2-1)


test = random.randrange(10000,40000)
print(test)

for i in range(test):
    n = random.randrange(2,10)
    rand_range = random.randrange(2,100)

    nums = Solution().randomArrayGenerator(n,rand_range)
    print(nums)
# nums = list(map(int, input("Enter an array: ").split()))
# print(f"Product of two maximum number sorting (i-1) and (j-1) is: {Solution().maxProductSorting(nums)}")
# print(f"Product of two maximum number searching (i-1) and (j-1) is: {Solution().maxProductSearching(nums)}")
# print(f"Product of two maximum number searching2 (i-1) and (j-1) is: {Solution().maxProductSearching2(nums)}")

    res1 = Solution().maxProductSearching(nums)
    res2 = Solution().maxProductSearching2(nums)
    res3 = Solution().maxProductSorting(nums)

    if res1 != res2 or res2 != res3:
        print("Error: Result mismatch", f"Res1 = {res1}, Res2 = {res2}, Res3 = {res3}")
        break

    else:
        print("Result Match")
print(test)