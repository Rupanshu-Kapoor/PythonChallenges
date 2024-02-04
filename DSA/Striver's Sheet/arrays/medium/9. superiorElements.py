"""
Superior Elements
https://www.codingninjas.com/studio/problems/superior-elements_6783446?leftPanelTabValue=PROBLEM

There is an integer array ‘a’ of size ‘n’.
An element is called a Superior Element if it is greater than all the elements present to its right.
You must return an array all Superior Elements in the array ‘a’.

Note:
The last element of the array is always a Superior Element.

Example
Input: a = [1, 2, 3, 2], n = 4
Output: 2 3
Explanation:
a[ 2 ] = 3 is greater than a[ 3 ]. Hence it is a Superior Element.
a[ 3 ] = 2 is the last element. Hence it is a Superior Element.
The final answer is in sorted order.
"""

from typing import *


def superiorElementsBF(a: List[int]) -> List[int]:
    """
    brute force: checking for every element, if all elements to its right are small or not
    :TC: O(N*N)
    :SC: O(N)
    :param a:
    :return:
    """
    ans = []
    for i in range(len(a) - 1, -1, -1):
        flag = 1
        for j in range(i, len(a)):
            if a[j] > a[i]:
                flag = 0
        if flag:
            ans.append(a[i])
    return ans


def superiorElements(a: List[int]) -> List[int]:
    """
    Optimal Solution: starting from right, we store the max value in maxi,
                        if current element is greater than maxi, that elemnet is superior element
                        and we update the maxi with current element
    :param a:
    :return:
    """
    maxi = a[-1]
    ans = [a[-1]]

    for i in range(len(a) - 2, -1, -1):
        if a[i] > maxi:
            maxi = a[i]
            ans.append(maxi)

    return ans


a = [1, 2, 3, 2]
print(superiorElementsBF(a))
