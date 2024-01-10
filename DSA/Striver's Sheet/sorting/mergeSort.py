"""
Merge Sort:https://www.codingninjas.com/studio/problems/merge-sort_5846?leftPanelTabValue=PROBLEM
Moderate
80/80
Problem statement
You are given the starting 'l' and the ending 'r' positions of the array 'ARR'.
You must sort the elements between 'l' and 'r'.
Note:
Change in the input array itself. So no need to return or print anything.
Example:
Input: ‘N’ = 7,
'ARR' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]

Explanation: After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
7
2 13 4 1 3 6 28
Sample Output 1:
1 2 3 4 6 13 28
Explanation of Sample Output 1:
After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
Sample Input 2:
5
9 3 6 2 0
Sample Output 2:
0 2 3 6 9
Explanation of Sample Output 2:
After applying 'merge sort' on the input array, the output is [0 2 3 6 9].
Constraints :
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
"""


def merger(arr, left, mid, right):
    temp_arr = []
    temp_left = left
    temp_mid = mid

    while temp_left <= mid and temp_mid < right:
        if arr[temp_mid + 1] < arr[temp_left]:
            temp_arr.append(arr[temp_mid + 1])
            temp_mid += 1
        else:
            temp_arr.append(arr[temp_left])
            temp_left += 1

    temp_arr.extend(arr[temp_left: mid + 1])
    temp_arr.extend(arr[temp_mid + 1: right + 1])
    arr[left:right + 1] = temp_arr


def mergeSort(arr, left, right):
    if left >= right:
        return
    mid = (right + left) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merger(arr, left, mid, right)


# a = [7, 3, 56, 89, 3, 4, 5, 6]
# a = [1, 2, 3, 4, 5, 6, 7, 8]
a = [3, 4, 5, 1, 2, 3]
print(a)
mergeSort(a, 0, len(a) - 1)
print(a)
