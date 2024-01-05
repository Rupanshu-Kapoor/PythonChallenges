"""
Linear search vs binary search:
"""
import timeit
import random


def lineraSeach(x: list[int], key):
    for i, j in enumerate(x):
        if j == key:
            return i + 1


def binarySearch(x: list[int], key):
    x.sort()
    i = 1
    while x:
        mid = len(x) // 2
        if x[mid] == key:
            return i
        elif key > x[mid]:
            x = x[mid + 1:]
        else:
            x = x[:mid]
        i += 1


def searchCompare():
    arr_size = int(input("Enter size of array: "))
    # key_element = int(input("Enter a key to find within array limit: "))
    # taking random from (arr_size)/2 to arr_size to get a random number in upper half range
    # to calculate time difference of both searches in a much real world problem scenario.

    key_element = random.randint(arr_size//2, arr_size)
    print(f"Random key element: {key_element} ")

    arr = [x + 1 for x in range(arr_size)]
    if key_element < arr_size:
        liner_index = lineraSeach(arr, key_element)
        binary_index = binarySearch(arr, key_element)
        print(f"Linear search took \"{liner_index}\" iteration to find key")
        print(f"Binary search took \"{binary_index}\" iteration to find key")

        binary_exe_time = timeit.timeit(lambda: binarySearch(arr, key_element), number=1000)
        print(f"Average execution time of binary search: {binary_exe_time}")
        liner_exe_time = timeit.timeit(lambda: lineraSeach(arr, key_element), number=1000)
        print(f"Average execution time of linear search is: {liner_exe_time}")
        print(f"Time difference of binary and linear search: {liner_exe_time - binary_exe_time}")


searchCompare()
