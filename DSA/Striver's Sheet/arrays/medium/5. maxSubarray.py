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


def maxSubarray(arr: [int]) -> int:
    """
    Kadane's Algo: similar to array-> medium-> 4.maxSubarraySum but this also prints the longest array
                    included two new variable start and end that tracks the longest subarray being formed
    :param arr:
    :return:
    """
    max_sum = float("-inf")
    curr_sum = 0
    start = end = 0  # initializing start and end to 0 to have an empty longest array
    for ele in range(len(arr)):

        curr_sum += arr[ele]
        if curr_sum >= max_sum:
            max_sum = curr_sum
            # if cur_sum > max_sum, then current element is being included in the longest array
            # so, we update end to current index
            end = ele

        if curr_sum < 0:
            curr_sum = 0
            # if sum is less than zero, we discard the previous sub-array
            # hence, updated start to next index to form a new sub-array
            start = ele + 1
    print(arr[start:end + 1])
    return max_sum


a = [-2, 1, -3, 4, -1, 2, 1, -15, 4]
print(maxSubarray(a))
