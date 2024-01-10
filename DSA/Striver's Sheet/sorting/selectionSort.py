def selectionSort(arr: list[int]):

    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(i, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return


a = [1,34,56,23,56,2,5,63,563,42,62,42,29]
print(a)
selectionSort(a)
print(a)
