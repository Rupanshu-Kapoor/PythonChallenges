"""
Bubble Sort:https://www.codingninjas.com/studio/problems/bubble-sort_624380?leftPanelTabValue=PROBLEM
Problem statement
You are given an integer array 'arr' of size 'N'.
You must sort this array using 'Bubble Sort'.
Note:
Change in the input array itself. You don't need to return or print the elements.
Example:
Input: ‘N’ = 7
'arr' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]

Explanation: After applying bubble sort on the input array, the output is [1 2 3 4 6 13 28].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
7
2 13 4 1 3 6 28
Sample Output 1:
1 2 3 4 6 13 28
Explanation of Sample Output 1:
After applying bubble sort on the input array, the output is [1 2 3 4 6 13 28].
Sample Input 2:
5
9 3 6 2 0
Sample Output 2:
0 2 3 6 9
Explanation of Sample Output 2:
After applying bubble sort on the input array, the output is [0 2 3 6 9].
Constraints :
1 <= N <= 10^3
0 <= arr[i] <= 10^9
Time Limit: 1 sec"""


def bubbleSort(arr: list[int]):
    size = len(arr)
    for i in range(size - 1):
        print(f"normal sort {i}")
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return


def optimisedBubbleSort(arr: list[int]):
    size = len(arr)
    for i in range(size - 1):
        print(f"optimised sort {i}")
        swap = False
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break

