"""
Second Largest Number:
https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?leftPanelTabValue=PROBLEM

Problem statement
You have been given an array ‘a’ of ‘n’ unique non-negative integers.
Find the second largest and second smallest element from the array.
Return the two elements (second largest and second smallest) as another array of size 2.

Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
4
3 4 5 2
Sample Output 1 :
4 3
Explanation For Sample Input 1 :
The second largest element after 5 is 4 only, and the second smallest element after 2 is 3.
Sample Input 2 :
5
4 5 3 6 7
Sample Output 2 :
6 4
Expected Time Complexity:
O(n), Where ‘n’ is the size of an input array ‘a’.
Constraints:
2 ≤ 'n' ≤ 10^5
0 ≤ 'a'[i] ≤ 10^9

Time limit: 1 sec

"""


def getSecondOrderElements(n: int, a: [int]) -> [int]:
    """
    brute force approach
    :TC: O(n log n + 2n)
    :param n: size of array
    :param a: array
    :return: returns second largest and second smallest
    """
    second_largest = -1
    second_smallest = -1
    a.sort(reverse=True)
    for i in a:
        if i != a[0]:
            second_largest = i
            break
    for i in range(n-1, -1, -1):
        if a[i] != a[-1]:
            second_smallest = a[i]
            break
    return [second_largest, second_smallest]


def getSecondOrderElements2(n: int, a: [int]) -> [int]:
    """
    better approach than brute force
    :TC: O(3n)
    :param n: size of array
    :param a: array
    :return: returns second largest and second smallest
    """
    largest = smallest = a[0]
    second_largest = -1
    second_smallest = float("inf")
    for i in range(1, n):
        if a[i] > largest:
            largest = a[i]
    for i in range(1,n):
        if a[i] < smallest:
            smallest = a[i]
    for i in a:
        if i > second_largest and i != largest:
            second_largest = i
        if i < second_smallest and i != smallest:
            second_smallest = i

    return [second_largest, second_smallest]


def getSecondOrderElements3(n: int, a: [int]) -> [int]:
    """
    Most optimal approach
    :TC: O(n)
    :param n: size of array
    :param a: array
    :return: returns second largest and second smallest
    """
    largest = smallest = a[0]
    second_largest = -float("inf")
    second_smallest = float("inf")

    for i in a:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_largest = i

    print(largest,smallest)

    return [second_largest, second_smallest]



n = 5
a = [1, 2, 3, 4, 5]
print(getSecondOrderElements3(n, a))
