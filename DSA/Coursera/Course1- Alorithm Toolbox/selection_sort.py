"""
learning algo selection sort
"""


def selectionSort(arr: list[int]) -> list[int]:
    for cur_index, cur_value in enumerate(arr):
        min_index = None
        min_value = float("inf")

        for ind in range(cur_index, len(arr)):
            if arr[ind] < min_value:
                min_index, min_value = ind, arr[ind]

        if min_value != cur_value:
            arr[cur_index], arr[min_index] = min_value, cur_value

    return arr


print(selectionSort([8, 5, 2, 4, 2]))
