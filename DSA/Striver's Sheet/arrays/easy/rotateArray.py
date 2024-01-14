"""
189. Rotate Array:https://leetcode.com/problems/rotate-array/description/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


def rotateArrayLeft(nums: [int], shifter: int) -> None:
    temp = nums[:shifter]
    for i in range(shifter, len(nums)):
        nums[i - shifter] = nums[i]

    nums[-shifter:] = temp



def rotateArrayRight(nums: [int], shifter: int) -> None:
    size = len(nums) - 1
    if shifter >= size + 1:
        shifter %= size + 1
    if not shifter:
        return
    temp = nums[-shifter:]
    for i in range(size - shifter, -1, -1):
        nums[i + shifter] = nums[i]

    nums[:shifter] = temp


def reverseArray(arr, start, end):
    i = start
    j = end
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def rotateArrayLeft2(nums: [int], shifter: int) -> None:
    """
    Optimised approach that doesn't take extra space and has space complexity of O(1)
    :param nums:
    :param shifter:
    :return:
    """
    size = len(nums)
    shifter %= size
    reverseArray(nums, 0, shifter - 1)
    reverseArray(nums, shifter, size - 1)
    reverseArray(nums, 0, size - 1)
    return


def rotateArrayRight2(nums: [int], shifter: int) -> None:
    """
    Optimised approach that doesn't take extra space and has space complexity of O(1)
    :param nums:
    :param shifter:
    :return:
    """
    size = len(nums)
    shifter %= size
    reverseArray(nums, size - shifter, size - 1)
    reverseArray(nums, 0, size - shifter - 1)
    reverseArray(nums, 0, size - 1)
    return


# rotateArrayLeft([1,2,3,4,5,6,7,8], 3)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
# rotateArrayRight2(a, 2)
rotateArrayLeft2(a, 2)
rotateArrayLeft(a,2)
print(a)


