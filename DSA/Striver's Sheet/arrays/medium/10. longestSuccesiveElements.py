"""
Longest Successive Elements:
https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740
There is an integer array ‘A’ of size ‘N’.
A sequence is successive when the adjacent elements of the sequence have a difference of 1.
You must return the length of the longest successive sequence.
Note:
You can reorder the array to form a sequence.
For example,
Input:
A = [5, 8, 3, 2, 1, 4], N = 6
Output:
5
Explanation:
The resultant sequence can be 1, 2, 3, 4, 5.
The length of the sequence is 5.
"""

from typing import *

def longestSuccessiveElements(a : List[int]) -> int:

    # maxi = count = 1
    # # a = list(set(sorted(a)))
    # a.sort()
    #
    # for i in range(len(a)-1):
    #     if a[i] + 1 == a[i+1]:
    #         count += 1
    #         maxi = max(maxi, count)
    #     elif a[i] == a[i+1]:
    #         continue
    #     else:
    #         maxi = max(maxi, count)
    #         count = 1
    # return maxi

    maxi = 1
    set_map = set()
    for i in a:
        set_map.add(i)
    for i in a:
        if i-1 in a:
            continue
        else:
            count = 1
            j = i
            while j+1 in set_map:
                count += 1
                j = j+1
            maxi = max(maxi, count)
    return maxi


a = [21,15, 6, 2, 1, 16, 4, 2, 29, 9, 12, 8, 5, 14, 21, 8, 12, 17, 16, 6, 26, 3]
print(longestSuccessiveElements(a))