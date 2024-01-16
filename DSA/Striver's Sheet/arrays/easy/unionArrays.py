"""
Merge 2 Sorted Array:
https://www.codingninjas.com/studio/problems/sorted-array_6613259?leftPanelTabValue=PROBLEM
Problem statement
Given two sorted arrays, ‘a’ and ‘b’, of size ‘n’ and ‘m’, respectively, return the union of the arrays.
The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order.

Note: 'a' and 'b' may contain duplicate elements, but the union array must contain unique elements.
Example:
Input: ‘n’ = 5 ‘m’ = 3
‘a’ = [1, 2, 3, 4, 6]
‘b’ = [2, 3, 5]

Output: [1, 2, 3, 4, 5, 6]

Explanation: Common elements in ‘a’ and ‘b’ are: [2, 3]
Distinct elements in ‘a’ are: [1, 4, 6]
Distinct elements in ‘b’ are: [5]
Union of ‘a’ and ‘b’ is: [1, 2, 3, 4, 5, 6]
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
5 3
1 2 3 4 6
2 3 5
Sample Output 1 :
1 2 3 4 5 6
Explanation Of Sample Input 1 :
Input: ‘n’ = 5 ‘m’ = 3
‘a’ = [1, 2, 3, 4, 6]
‘b’ = [2, 3, 5]

Output: [1, 2, 3, 4, 5, 6]

Explanation: Common elements in ‘a’ and ‘b’ are: [2, 3]
Distinct elements in ‘a’ are: [1, 4, 6]
Distinct elements in ‘b’ are: [5]
Union of ‘a’ and ‘b’ is: [1, 2, 3, 4, 5, 6]
Sample Input 2:
4 3
1 2 3 3
2 2 4
Sample Output 2:
1 2 3 4
Explanation Of Sample Input 2 :
Input: ‘n’ = 5 ‘m’ = 3
‘a’ = [1, 2, 3, 3]
‘b’ = [2, 2, 4]

Output: [1, 2, 3, 4]

Explanation: Common elements in ‘a’ and ‘b’ are: [2]
Distinct elements in ‘a’ are: [1, 3]
Distinct elements in ‘b’ are: [4]
Union of ‘a’ and ‘b’ is: [1, 2, 3, 4]
Expected Time Complexity:
O(( N + M )), where 'N' and ‘M’ are the sizes of Array ‘A’ and ‘B’.
Constraints :
1 <= 'n', 'm' <= 10^5
-10^9 <= 'a'[i], 'b'[i] <= 10^9

Time Limit: 1 sec
"""


def sortedArrayBF(a: [int], b: [int]) -> [int]:
    """
    Brute force approach
    :param a:
    :param b:
    :return:
    """
    sorted_array = list(set(a + b))
    sorted_array.sort()
    return sorted_array


def sortedArray1(a: [int], b: [int]) -> [int]:
    sorted_array = []

    for i in range(len(a)):
        if a[i] not in sorted_array:
            sorted_array.append(a[i])
    for i in range(len(b)):
        if b[i] not in sorted_array:
            sorted_array.append(b[i])
    print(sorted_array)
    return sorted_array


def sortedArray2(a: [int], b: [int]) -> [int]:
    """
    :TC: O(m+n) O(log(m+n))
    inserting elements in dictionary take nlogn
    and there can be n+m unique elements in the worst case.
    Hence, inserting elements in the union list will take O(m+n)
    :param a:
    :param b:
    :return:
    """
    freq = {}
    union = []

    for num in a:
        freq[num] = freq.get(num, 0) + 1
    for num in b:
        freq[num] = freq.get(num, 0) + 1
    for num in freq:
        union.append(num)
    return union


def sortedArrayOP(a: [int], b: [int]) -> [int]:
    union = []
    last_inserted = None
    i = j = 0

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            if a[i] != last_inserted:
                union.append(a[i])
                last_inserted = a[i]
            i += 1
        elif a[i] > b[j]:
            if b[j] != last_inserted:
                union.append(b[j])
                last_inserted = b[j]
            j += 1

    while i < len(a):
        if a[i] != last_inserted:
            union.append(a[i])
            last_inserted = a[i]
        i += 1
    while j < len(b):
        if b[j] != last_inserted:
            union.append(b[j])
            last_inserted = b[j]
        j += 1

    return union


a1 = [1, 2, 3, 4, 5, 6]
b1 = [2, 3, 5]
# print(sortedArray1(a1, b1))
print(sortedArrayOP(a1, b1))
# sortedArrayOP(a1,b1)
