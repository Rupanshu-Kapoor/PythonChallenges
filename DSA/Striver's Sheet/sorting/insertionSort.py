def insertionSort(arr: list[int]):
    for i in range(1, len(arr)):
        j = i
        while j >= 1 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# a = [3,2,5,4,1]
a = [1,2,3,4,5]
# a = [1, 34, 56, 23, 56, 2, 5, 63, 563, 42, 62, 42, 29]

print(a)
insertionSort(a)
print(a)
