def bubbleSort(arr: list[int]):

    size = len(arr)
    for i in range(size-1):
        print(f"normal sort {i}")
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return


def optimisedBubbleSort(arr: list[int]):

    size = len(arr)
    for i in range(size-1):
        print(f"optimised sort {i}")
        swap = False
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break


# a = [1,3,2,5,3,4,6]
a = [5,4,3,2,1]
# a = [1,34,56,23,56,2,5,63,563,42,62,42,29]
b = a.copy()
bubbleSort(a)
optimisedBubbleSort(b)
print(a)
print(b)