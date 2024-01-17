"""
Longest Subarray With Sum K
https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399
Problem statement
You are given an array 'a' of size 'n' and an integer 'k'.

Find the length of the longest subarray of 'a' whose sum is equal to 'k'.
Example :
Input: ‘n’ = 7 ‘k’ = 3
‘a’ = [1, 2, 3, 1, 1, 1, 1]

Output: 3
Explanation: Subarrays whose sum = ‘3’ are:
[1, 2], [3], [1, 1, 1] and [1, 1, 1]

Here, the length of the longest subarray is 3, which is our final answer.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
7 3
1 2 3 1 1 1 1
Sample Output 1 :
3
Explanation Of Sample Input 1 :
Subarrays whose sum = ‘3’ are:
[1, 2], [3], [1, 1, 1] and [1, 1, 1]
Here, the length of the longest subarray is 3, which is our final answer.

Sample Input 2 :
4 2
1 2 1 3
Sample Output 2 :
1

Sample Input 3 :
5 2
2 2 4 1 2
Sample Output 3 :
1

Expected time complexity :
The expected time complexity is O(n).

Constraints :
1 <= 'n' <= 5 * 10 ^ 6
1 <= 'k' <= 10^18
0 <= 'a[i]' <= 10 ^ 9

Time Limit: 1-second
"""


def longestSubarrayWithSumK1(a: [int], k: int) -> int:
    max_len = 0
    for i in range(len(a)):
        total = 0
        for j in range(i, len(a)):
            total += a[j]
            if total == k:
                max_len = max(max_len, j - i + 1)
            elif total > k:
                break

    return max_len


def longestSubarrayWithSumK2(a: [int], k: int) -> int:
    pass
    n = len(a)  # size of the array

    presum_map = {}
    total = 0
    max_len = 0

    for i in range(n):
        total += a[i]  # calculate sum till index i

        # if sum = k, update the max_len
        if total == k:
            max_len = max(max_len, i + 1)

        # calculate the sum of remaining part i.e. x-k
        rem = total - k

        # calculate the length and update max_len
        if rem in presum_map:
            length = i - presum_map[rem]
            max_len = max(max_len, length)

        # update the map
        if total not in presum_map:
            presum_map[total] = i

    return max_len


def longestSubarrayWithSumKOP(a: [int], k: int) -> int:
    total = 0
    right = left = 0
    max_len = 0

    # iterate through whole array
    while right < len(a):

        # total till ith index
        total += a[right]

        # if total > k, then  move the left pointer till total <= k
        # and reduce total by the jth element
        while total > k:
            total -= a[left]
            left += 1

        # if total = k, then update the max_length
        if total == k:
            length = right - left + 1
            max_len = max(max_len, length)
        right += 1
    return max_len


a1 = [-50, 0, 52]
k1 = 2
print(longestSubarrayWithSumK2(a1, k1))
print(longestSubarrayWithSumKOP(a1, k1))
