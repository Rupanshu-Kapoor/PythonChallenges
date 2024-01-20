"""
 Sort An Array of 0s, 1s and 2s
https://www.codingninjas.com/studio/problems/sort-an-array-of-0s-1s-and-2s_892977
You have been given an array/list 'arr' consisting of 'n' elements.
Each element in the array is either 0, 1 or 2.
Sort this array/list in increasing order.
Do not make a new array/list. Make changes in the given array/list.

Example :
Input: 'arr' = [2, 2, 2, 2, 0, 0, 1, 0]

Output: Final 'arr' = [0, 0, 0, 1, 2, 2, 2, 2]

Explanation: The array is sorted in increasing order.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
8
2 2 2 2 0 0 1 0


Sample Output 1:
0 0 0 1 2 2 2 2
Explanation of sample input 1 :
The initial array 'arr' is [2, 2, 2, 2, 0, 0, 1, 0].
After sorting the array in increasing order, 'arr' is equal to:
[0, 0, 0, 1, 2, 2, 2, 2]

Sample Input 2:
5
1 1 1 1 1
Sample Output 2:
1 1 1 1 1
Expected time complexity :
The expected time complexity is O(n).

Constraints:
1 <= 'n' <= 10 ^ 40
0 <= 'arr[i]' <= 2
Time limit: 1 second
"""


def sortArray(arr, n):
    """
    brute force: using two loops to sort using bubble sort
    :TC: O(n*n)
    :SC: O(1)
    :param arr:
    :param n:
    :return:
    """
    for i in range(n):
        for j in range(i, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


def sortArray2(arr, n):
    """
    using hashing
    :TC: O(n+3)
    :SC: O(n)
    :param arr:
    :param n:
    :return:
    """
    hash_map = {}

    for i in arr:
        # counting occurrence of 1,2,3 and storing them in hash_map
        hash_map[i] = hash_map.get(i, 0) + 1
    ind1 = 0
    ind2 = 0
    # looping for i = 0,1,2
    for i in range(3):
        # if i exist in hash_map then modifying the array according to the count of i
        if i in hash_map:
            ind2 += hash_map[i]
            arr[ind1:ind2] = [i] * hash_map[i]
            ind1 = ind2


def sortArrayOP(arr, n):
    """
    DUTCH NATIONAL FLAG ALGO
    the main idea is:
        keep all 0 from index 0 to low-1
        keep all 1 from index low to mid-1
        keep all 2 from index high to n-1
        and all unsorted index remains between mid and high

    :TC: O(n)
    :SC: O(1)
    :param arr:
    :param n:
    :return:
    """

    n = len(arr)
    # initializing low and mid to 0th index and high to (n-1)th index i.e last index
    low = mid = 0
    high = n - 1

    # we sort all the index between mid and high and move mid and high pointer accordingly
    while mid <= high:

        # if mid = 0, swap that element with low index and increase mid and low
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1

        # if mid = 1, its already sorted, increase the mid pointer
        elif arr[mid] == 1:
            mid += 1

        # if mid = 2, swap it with high index and decrease the high index
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


a = [2, 2, 2, 2, 0, 0, 1, 0]
print(a)
sortArrayOP(a, len(a))
print(a)
