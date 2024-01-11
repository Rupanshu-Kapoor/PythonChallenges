"""
Largest Element in the Array:https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279

Easy
Problem statement
Given an array ‘arr’ of size ‘n’ find the largest element in the array.
Example:

Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: 5

Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
Detailed explanation ( Input/output format, Notes, Images )
Sample input 1:
6
4 7 8 6 7 6
Sample output 1:
8
Explanation of sample input 1:
The answer is 8.
From {4 7 8 6 7 6}, 8 is the largest element.
Sample input 2:
8
5 9 3 4 8 4 3 10
Sample output 2:
10
Expected Time Complexity:
O(n), Where ‘n’ is the size of an input array ‘arr’.
Constraints :
1 <= 'n' <= 10^5
1 <= 'arr[i]' <= 10^9

Time Limit: 1 sec"""


def largestElement(arr: [], n: int) -> int:
    """
    Brute force approach
    :TC: O(n log n)
    :param arr: array of numbers
    :param n: size of array
    :return: Largest element in the array
    """
    arr.sort()
    return arr[-1]


def largestElement2(arr: [], n: int) -> int:
    """
    Optimised approach
    :TC: O(n)
    :param arr: array of numbers
    :param n: size of array
    :return: Largest element in the array
    """
    max_element = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element


n = 5
a = [1, 2, 3, 4, 5]
print(largestElement(a, n))
