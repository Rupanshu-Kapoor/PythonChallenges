"""
learning algo merge sort
"""
import selection_sort
import timeit
import random


def merger(a: list[int], b: list[int]) -> list[int]:
    result = [0] * (len(a) + len(b))
    i = j = k = 0
    while a and b:
        if a[i] <= b[j]:
            result[k] = a[i]
            a.pop(i)
            k += 1
        else:
            result[k] = b[j]
            b.pop(j)
            k += 1

    if not a:
        while b:
            result[k] = b[j]
            b.pop(j)
            k += 1
    else:
        while a:
            result[k] = a[i]
            a.pop(i)
            k += 1

    return result


def mergerSort(arr: list[int]) -> list[int]:
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    a = mergerSort(arr[:mid])
    b = mergerSort(arr[mid:])
    result = merger(a, b)
    return result


# Driver code
arr_range = random.randint(1000, 10000)
print("Array range:", arr_range)
arr = []
for i in range(arr_range):
    arr.append(random.randint(0, 100))
print(arr)

exe_merge_sor = timeit.timeit(lambda: mergerSort(arr), number=1000)
print(f"average execution time for merge sort is: {exe_merge_sor}")

exe_selection_sort = timeit.timeit(lambda: selection_sort.selectionSort(arr), number=1000)
print(f"average execution time for selection sort is: {exe_selection_sort}")

print(f"time difference: {exe_selection_sort - exe_merge_sor}")
print(f"Selection sort takes {round((exe_selection_sort-exe_merge_sor)/exe_merge_sor *100,2)}% more time than merge sort")


"""
AN INTERESTING RESULT

Array range: 4718
[20, 52, 39, 11, 92, 67, 95, 28, 50, 36, 20, 6, 100, 17, 54, 54, 17, 0, 31, 5, 55, 40, 66, 85, 10, 32, 94, 73, 45, 89, 75, 58, 55, 62, 32, 95, 29, 54, 57, 71, 0, 44, 15, 23, 4, 39, 18, 96, 50, 92, 54, 56, 3, 40, 56, 39, 33, 49, 9, 59, 9, 39, 67, 57, 92, 5, 58, 79, 1, 78, 34, 45, 28, 32, 57, 87, 60, 57, 1, 19, 94, 61, 80, 91, 62, 53, 46, 14, 26, 47, 66, 56, 84, 56, 83, 92, 78, 71, 58, 93, 54, 79, 36, 26, 7, 20, 38, 52, 15, 3, 14, 86, 72, 96, 56, 96, 87, 54, 87, 64, 73, 50, 71, 87, 18, 68, 77, 47, 20, 81, 32, 76, 93, 49, 87, 97, 44, 58, 48, 57, 45, 0, 31, 98, 45, 26, 68, 65, 95, 18, 74, 61, 26, 45, 94, 59, 32, 85, 14, 23, 46, 56, 22, 21, 51, 68, 48, 87, 26, 83, 48, 28, 63, 13, 7, 7, 28, 16, 83, 33, 27, 91, 76, 50, 58, 100, 72, 25, 99, 33, 92, 5, 10, 94, 38, 31, 57, 13, 25, 57, 44, 37, 16, 80, 10, 88, 85, 37, 19, 40, 8, 93, 96, 84, 75, 2, 53, 47, 70, 27, 53, 73, 32, 48, 81, 12, 62, 97, 68, 91, 54, 7, 10, 35, 5, 64, 30, 51, 84, 16, 12, 69, 56, 1, 9, 96, 92, 95, 14, 68, 86, 21, 15, 51, 47, 32, 31, 97, 20, 78, 42, 97, 52, 82, 38, 84, 21, 95, 59, 68, 8, 70, 5, 81, 48, 13, 23, 28, 100, 6, 95, 55, 15, 9, 51, 56, 7, 54, 62, 35, 21, 16, 81, 65, 51, 69, 44, 84, 16, 61, 60, 33, 14, 67, 18, 18, 26, 34, 98, 100, 87, 1, 4, 96, 39, 98, 65, 100, 23, 10, 7, 64, 66, 62, 87, 48, 59, 20, 65, 80, 35, 83, 49, 5, 83, 39, 71, 92, 68, 64, 83, 93, 87, 31, 96, 0, 2, 17, 84, 63, 31, 48, 61, 4, 10, 43, 53, 85, 65, 65, 9, 62, 44, 31, 93, 25, 75, 58, 10, 30, 5, 61, 48, 26, 91, 81, 51, 11, 6, 46, 18, 88, 1, 82, 15, 28, 62, 99, 94, 39, 45, 69, 20, 90, 32, 89, 87, 24, 79, 94, 19, 28, 55, 83, 53, 94, 54, 9, 30, 26, 91, 91, 48, 4, 47, 74, 66, 65, 17, 100, 34, 2, 64, 49, 31, 4, 87, 94, 26, 5, 32, 10, 17, 53, 72, 52, 95, 83, 64, 50, 47, 60, 26, 56, 60, 9, 44, 82, 65, 96, 85, 17, 37, 73, 18, 82, 6, 26, 9, 27, 76, 46, 41, 42, 52, 55, 17, 7, 77, 89, 100, 63, 67, 62, 92, 81, 72, 42, 33, 81, 62, 41, 70, 51, 26, 48, 78, 15, 25, 31, 31, 1, 36, 57, 100, 36, 24, 27, 37, 3, 19, 97, 1, 74, 36, 45, 93, 14, 18, 95, 35, 8, 85, 58, 58, 100, 1, 40, 62, 73, 1, 84, 99, 0, 3, 62, 98, 40, 85, 59, 12, 25, 49, 52, 21, 8, 19, 76, 8, 2, 84, 47, 37, 7, 10, 37, 43, 10, 55, 67, 21, 69, 62, 15, 60, 59, 45, 89, 21, 51, 61, 84, 35, 94, 68, 99, 7, 47, 27, 93, 76, 80, 53, 51, 69, 65, 11, 0, 18, 11, 76, 8, 42, 55, 20, 8, 37, 46, 43, 34, 43, 86, 94, 57, 1, 56, 31, 63, 57, 88, 86, 24, 37, 67, 72, 74, 64, 3, 66, 15, 75, 75, 89, 27, 28, 6, 61, 98, 15, 52, 53, 0, 49, 14, 39, 89, 3, 77, 74, 33, 8, 77, 45, 69, 34, 16, 58, 32, 26, 19, 99, 21, 88, 10, 67, 4, 8, 53, 89, 17, 57, 90, 81, 60, 39, 94, 50, 16, 78, 69, 74, 35, 55, 58, 68, 85, 56, 10, 9, 64, 38, 77, 16, 39, 89, 96, 32, 32, 98, 99, 25, 80, 78, 11, 53, 61, 5, 35, 91, 41, 62, 45, 42, 22, 8, 45, 62, 50, 33, 64, 100, 85, 8, 49, 39, 26, 54, 97, 90, 8, 17, 84, 63, 45, 2, 46, 78, 17, 94, 19, 37, 84, 57, 46, 3, 12, 34, 36, 38, 95, 91, 62, 98, 82, 50, 79, 96, 34, 4, 99, 99, 27, 75, 55, 97, 50, 46, 100, 100, 82, 55, 44, 14, 60, 86, 61, 11, 33, 100, 93, 44, 30, 79, 84, 21, 58, 87, 45, 12, 50, 23, 36, 87, 68, 90, 74, 80, 10, 45, 29, 68, 86, 76, 4, 89, 56, 11, 64, 29, 100, 93, 24, 52, 0, 53, 7, 50, 53, 89, 30, 83, 19, 16, 62, 98, 40, 85, 44, 67, 53, 97, 86, 29, 0, 56, 86, 29, 5, 58, 93, 99, 80, 91, 80, 16, 86, 94, 9, 4, 27, 64, 45, 64, 21, 66, 16, 21, 53, 97, 13, 50, 91, 0, 73, 76, 51, 64, 67, 90, 51, 97, 11, 23, 85, 96, 72, 21, 43, 94, 48, 56, 82, 7, 61, 79, 88, 21, 58, 15, 52, 30, 61, 23, 29, 80, 98, 78, 8, 31, 92, 93, 0, 6, 0, 78, 44, 19, 61, 13, 65, 85, 67, 28, 28, 23, 15, 66, 83, 17, 90, 45, 62, 12, 86, 30, 37, 65, 4, 49, 10, 73, 35, 15, 51, 82, 5, 21, 74, 70, 88, 49, 81, 56, 53, 61, 93, 55, 39, 11, 42, 12, 18, 1, 86, 5, 56, 48, 93, 13, 64, 28, 98, 23, 70, 81, 56, 94, 97, 95, 78, 69, 32, 0, 45, 59, 39, 68, 55, 48, 57, 81, 7, 68, 39, 62, 39, 6, 100, 78, 41, 48, 31, 36, 53, 55, 86, 32, 77, 75, 95, 24, 87, 79, 34, 86, 31, 13, 42, 65, 87, 98, 89, 5, 46, 85, 41, 86, 42, 48, 73, 58, 93, 17, 98, 91, 30, 45, 6, 87, 59, 39, 91, 16, 35, 43, 49, 79, 53, 75, 28, 6, 43, 12, 51, 94, 23, 49, 61, 72, 82, 63, 78, 58, 79, 29, 77, 71, 12, 86, 39, 67, 52, 9, 79, 98, 14, 45, 53, 4, 63, 0, 40, 62, 65, 23, 95, 78, 45, 6, 71, 35, 13, 49, 59, 77, 72, 41, 3, 26, 4, 54, 20, 19, 97, 87, 63, 85, 52, 65, 84, 48, 8, 94, 8, 96, 89, 24, 25, 100, 96, 35, 66, 98, 36, 56, 77, 43, 41, 71, 6, 73, 5, 83, 12, 36, 54, 21, 63, 38, 98, 11, 13, 7, 61, 89, 42, 61, 10, 87, 46, 5, 60, 36, 41, 95, 14, 23, 15, 96, 62, 93, 66, 38, 46, 8, 47, 97, 42, 50, 24, 54, 23, 36, 47, 78, 31, 2, 75, 58, 66, 44, 46, 23, 62, 90, 95, 50, 85, 95, 51, 82, 57, 93, 21, 3, 52, 53, 9, 91, 90, 70, 86, 42, 100, 45, 46, 25, 64, 11, 94, 54, 6, 87, 10, 64, 23, 65, 21, 98, 96, 12, 65, 11, 84, 20, 66, 0, 75, 6, 33, 74, 38, 60, 35, 14, 80, 94, 72, 29, 29, 47, 74, 3, 9, 60, 17, 29, 47, 26, 62, 66, 67, 24, 44, 14, 26, 39, 26, 78, 79, 49, 35, 69, 22, 96, 34, 33, 21, 42, 10, 41, 81, 64, 89, 22, 75, 2, 94, 30, 17, 4, 31, 73, 57, 43, 31, 77, 67, 92, 40, 38, 75, 53, 79, 65, 11, 29, 16, 62, 44, 5, 24, 90, 62, 23, 21, 21, 15, 56, 56, 55, 2, 89, 61, 97, 76, 41, 62, 83, 74, 7, 77, 27, 92, 73, 93, 98, 57, 7, 63, 18, 19, 2, 39, 13, 48, 73, 5, 25, 73, 51, 53, 64, 91, 50, 71, 60, 7, 81, 43, 20, 76, 42, 63, 20, 20, 17, 83, 21, 90, 18, 87, 31, 83, 30, 92, 79, 17, 83, 83, 13, 70, 51, 25, 84, 55, 49, 60, 12, 37, 16, 32, 27, 67, 51, 71, 82, 93, 92, 96, 14, 86, 77, 97, 60, 96, 39, 47, 64, 45, 57, 30, 7, 60, 69, 54, 64, 79, 58, 20, 82, 49, 21, 97, 21, 18, 20, 45, 64, 89, 43, 27, 64, 47, 4, 90, 20, 59, 75, 71, 53, 17, 70, 74, 0, 25, 11, 97, 72, 46, 10, 7, 84, 45, 91, 15, 5, 24, 21, 30, 13, 81, 35, 97, 99, 51, 90, 48, 51, 79, 75, 10, 79, 3, 43, 89, 98, 60, 35, 95, 22, 54, 98, 22, 96, 88, 16, 96, 100, 45, 77, 89, 7, 89, 83, 77, 84, 57, 91, 5, 88, 84, 88, 42, 8, 83, 26, 4, 86, 60, 4, 19, 47, 62, 86, 6, 68, 9, 95, 33, 95, 65, 87, 88, 62, 83, 72, 42, 42, 62, 13, 43, 47, 59, 43, 36, 5, 56, 58, 54, 33, 96, 31, 3, 60, 98, 48, 92, 88, 44, 81, 28, 95, 90, 45, 95, 49, 16, 29, 34, 89, 54, 58, 0, 16, 34, 6, 27, 99, 14, 100, 49, 82, 29, 17, 27, 63, 93, 14, 13, 47, 21, 79, 84, 92, 74, 61, 24, 84, 62, 17, 2, 40, 2, 52, 5, 86, 89, 69, 96, 62, 46, 60, 0, 83, 30, 79, 80, 37, 4, 97, 58, 45, 10, 91, 99, 72, 63, 95, 26, 92, 27, 32, 7, 65, 66, 91, 17, 82, 20, 24, 40, 15, 0, 53, 20, 78, 44, 19, 81, 35, 72, 76, 54, 79, 51, 48, 35, 76, 74, 6, 72, 79, 31, 64, 15, 97, 3, 69, 77, 0, 99, 36, 0, 88, 33, 9, 67, 47, 92, 28, 16, 98, 98, 81, 20, 9, 44, 11, 69, 77, 29, 62, 78, 20, 55, 13, 36, 55, 68, 37, 80, 31, 20, 39, 26, 63, 16, 40, 32, 54, 43, 65, 14, 42, 42, 89, 60, 8, 98, 45, 100, 12, 18, 82, 75, 72, 0, 62, 54, 68, 53, 85, 21, 4, 10, 37, 78, 75, 40, 10, 89, 62, 93, 86, 19, 1, 53, 86, 55, 71, 99, 50, 54, 98, 26, 50, 4, 58, 99, 30, 72, 61, 35, 22, 37, 39, 78, 84, 47, 33, 61, 67, 81, 70, 70, 3, 78, 20, 16, 47, 93, 89, 46, 60, 65, 32, 51, 34, 32, 73, 94, 8, 4, 57, 31, 11, 13, 0, 77, 70, 51, 51, 62, 7, 11, 54, 47, 26, 86, 50, 48, 96, 78, 12, 92, 19, 71, 42, 26, 56, 39, 22, 96, 6, 38, 91, 21, 38, 27, 75, 26, 40, 87, 30, 88, 78, 8, 31, 25, 67, 36, 30, 30, 31, 61, 94, 65, 94, 60, 47, 81, 51, 18, 79, 68, 4, 98, 21, 15, 37, 3, 49, 80, 38, 7, 93, 74, 52, 29, 76, 37, 7, 16, 7, 86, 97, 59, 63, 42, 15, 59, 8, 70, 95, 23, 21, 43, 29, 79, 37, 48, 86, 32, 34, 18, 47, 92, 94, 76, 44, 75, 67, 19, 94, 29, 81, 63, 5, 46, 91, 67, 38, 54, 95, 65, 4, 65, 55, 35, 53, 71, 47, 38, 65, 49, 95, 24, 67, 78, 18, 77, 72, 78, 6, 45, 72, 87, 78, 96, 32, 24, 7, 27, 64, 10, 91, 57, 69, 14, 3, 94, 22, 96, 35, 46, 52, 96, 24, 29, 64, 27, 27, 100, 29, 17, 75, 33, 5, 96, 41, 96, 94, 61, 20, 47, 28, 74, 40, 86, 14, 13, 12, 97, 24, 0, 0, 47, 64, 4, 76, 31, 1, 98, 83, 36, 58, 89, 90, 39, 47, 67, 66, 100, 51, 40, 55, 76, 1, 73, 6, 33, 39, 17, 38, 61, 65, 2, 59, 86, 26, 97, 56, 71, 79, 5, 90, 83, 31, 40, 46, 59, 54, 72, 30, 76, 28, 83, 98, 83, 8, 23, 99, 66, 22, 16, 85, 61, 13, 73, 90, 78, 22, 4, 82, 30, 72, 64, 63, 95, 6, 95, 4, 5, 79, 52, 84, 66, 17, 23, 15, 53, 49, 71, 49, 28, 97, 94, 68, 7, 10, 45, 27, 31, 46, 67, 89, 36, 58, 25, 80, 8, 29, 69, 69, 1, 28, 87, 97, 2, 27, 73, 52, 59, 19, 86, 73, 32, 82, 84, 34, 9, 11, 72, 68, 70, 61, 64, 5, 69, 95, 83, 67, 91, 71, 77, 14, 38, 14, 78, 42, 53, 71, 4, 74, 86, 46, 11, 25, 3, 91, 87, 12, 78, 70, 82, 96, 20, 55, 48, 80, 44, 5, 23, 83, 12, 13, 36, 44, 87, 1, 25, 32, 25, 79, 7, 81, 33, 10, 49, 52, 35, 86, 31, 26, 23, 75, 94, 87, 87, 40, 42, 37, 47, 60, 43, 42, 52, 68, 88, 69, 62, 17, 54, 45, 0, 20, 86, 66, 2, 79, 98, 93, 51, 87, 27, 81, 4, 43, 67, 41, 76, 45, 83, 38, 44, 20, 11, 58, 56, 97, 29, 76, 2, 85, 58, 61, 93, 78, 86, 92, 71, 71, 98, 48, 56, 80, 81, 90, 42, 34, 4, 44, 42, 48, 20, 30, 46, 87, 86, 27, 20, 96, 57, 93, 68, 31, 87, 87, 8, 33, 19, 10, 8, 67, 91, 66, 51, 83, 84, 40, 47, 57, 10, 41, 32, 77, 0, 67, 15, 5, 66, 40, 78, 40, 100, 26, 23, 57, 12, 41, 19, 69, 55, 0, 6, 27, 27, 65, 42, 73, 28, 89, 78, 54, 100, 77, 50, 60, 46, 31, 63, 70, 76, 69, 33, 45, 64, 79, 89, 96, 41, 18, 45, 6, 15, 10, 49, 71, 28, 16, 47, 70, 88, 49, 29, 54, 73, 77, 24, 31, 76, 15, 18, 6, 12, 21, 91, 1, 58, 58, 74, 64, 96, 52, 91, 65, 41, 78, 98, 89, 76, 61, 21, 69, 54, 100, 82, 55, 90, 73, 56, 35, 72, 36, 41, 46, 20, 20, 9, 22, 64, 28, 22, 37, 57, 25, 43, 90, 94, 52, 11, 52, 76, 9, 82, 53, 58, 10, 18, 75, 68, 29, 32, 27, 18, 7, 17, 96, 71, 38, 45, 63, 92, 37, 61, 8, 18, 97, 60, 63, 68, 76, 30, 74, 93, 100, 71, 3, 20, 10, 47, 82, 67, 29, 61, 47, 44, 81, 69, 88, 2, 85, 47, 43, 99, 69, 37, 27, 80, 40, 40, 75, 14, 44, 31, 38, 68, 36, 22, 33, 10, 78, 55, 34, 21, 39, 98, 39, 50, 85, 29, 67, 8, 21, 19, 93, 97, 9, 35, 27, 7, 51, 60, 85, 100, 97, 87, 73, 30, 29, 27, 15, 21, 55, 10, 76, 76, 10, 9, 80, 93, 69, 38, 77, 95, 43, 98, 29, 93, 87, 86, 24, 48, 72, 95, 58, 55, 28, 12, 48, 80, 24, 63, 62, 87, 17, 21, 19, 87, 75, 42, 28, 92, 89, 58, 19, 63, 6, 36, 96, 83, 90, 6, 52, 98, 17, 1, 63, 47, 81, 84, 35, 82, 24, 64, 84, 5, 13, 69, 21, 70, 68, 13, 68, 37, 42, 69, 18, 23, 53, 59, 18, 82, 47, 88, 9, 29, 77, 96, 5, 5, 78, 1, 74, 94, 35, 38, 98, 45, 23, 39, 23, 25, 11, 99, 14, 60, 3, 97, 15, 32, 12, 2, 46, 85, 60, 10, 72, 89, 100, 6, 57, 37, 4, 30, 19, 2, 77, 91, 34, 14, 10, 31, 66, 75, 8, 81, 41, 15, 96, 27, 3, 42, 53, 53, 97, 81, 61, 62, 92, 51, 52, 59, 71, 48, 47, 11, 20, 83, 11, 32, 82, 79, 62, 14, 59, 49, 26, 90, 7, 68, 40, 24, 53, 27, 0, 97, 0, 50, 38, 79, 29, 1, 46, 7, 22, 47, 86, 9, 94, 10, 59, 4, 59, 81, 58, 46, 66, 86, 56, 24, 94, 30, 66, 69, 63, 51, 2, 83, 82, 65, 29, 65, 0, 0, 75, 15, 92, 48, 82, 99, 10, 34, 81, 97, 19, 37, 80, 8, 5, 99, 16, 34, 90, 6, 11, 24, 3, 29, 61, 96, 0, 85, 76, 35, 37, 35, 90, 89, 24, 55, 19, 2, 48, 14, 87, 89, 15, 8, 40, 18, 7, 35, 71, 44, 43, 93, 54, 69, 80, 21, 32, 36, 49, 82, 37, 91, 42, 94, 44, 48, 23, 20, 41, 100, 89, 54, 33, 41, 91, 90, 38, 8, 2, 39, 37, 57, 99, 23, 88, 60, 61, 50, 59, 81, 8, 53, 36, 14, 89, 93, 98, 31, 92, 41, 29, 21, 65, 99, 44, 23, 91, 44, 8, 91, 91, 12, 63, 60, 46, 31, 40, 93, 37, 78, 71, 100, 20, 14, 28, 43, 27, 99, 56, 12, 75, 0, 18, 88, 57, 0, 43, 83, 2, 45, 70, 38, 22, 37, 7, 0, 88, 34, 70, 93, 86, 82, 91, 24, 25, 71, 53, 16, 75, 28, 36, 42, 27, 37, 26, 22, 39, 2, 18, 86, 99, 56, 53, 47, 7, 75, 79, 95, 25, 45, 5, 30, 60, 46, 17, 54, 10, 12, 26, 99, 71, 55, 48, 5, 5, 91, 85, 28, 6, 71, 40, 72, 12, 36, 35, 52, 75, 13, 79, 37, 82, 5, 34, 1, 83, 20, 86, 68, 39, 6, 6, 73, 41, 73, 0, 15, 83, 83, 92, 0, 55, 39, 90, 33, 89, 14, 49, 49, 7, 11, 82, 17, 66, 36, 67, 35, 23, 95, 28, 71, 71, 79, 22, 41, 76, 27, 9, 83, 29, 39, 44, 33, 1, 75, 81, 25, 99, 100, 58, 31, 31, 77, 55, 74, 68, 69, 38, 70, 30, 89, 42, 37, 16, 4, 1, 83, 58, 27, 87, 51, 50, 65, 22, 85, 22, 62, 43, 71, 55, 47, 87, 28, 84, 21, 91, 73, 68, 14, 11, 85, 82, 71, 30, 100, 98, 72, 87, 98, 23, 23, 45, 37, 66, 43, 47, 30, 48, 27, 100, 28, 33, 26, 13, 61, 12, 12, 14, 73, 46, 52, 75, 86, 62, 45, 85, 53, 30, 90, 55, 96, 97, 10, 41, 69, 16, 54, 85, 60, 87, 44, 78, 77, 80, 50, 17, 85, 88, 41, 59, 69, 84, 29, 43, 7, 97, 34, 5, 44, 97, 84, 76, 65, 83, 1, 2, 67, 23, 45, 33, 23, 66, 30, 34, 100, 32, 60, 100, 96, 53, 41, 28, 33, 61, 5, 78, 96, 96, 34, 42, 80, 53, 16, 86, 20, 98, 35, 45, 27, 32, 6, 52, 16, 85, 75, 64, 17, 70, 27, 72, 11, 24, 61, 100, 5, 62, 17, 75, 64, 10, 47, 1, 42, 8, 79, 89, 18, 69, 13, 26, 52, 74, 50, 7, 61, 54, 80, 62, 11, 73, 18, 47, 63, 20, 13, 93, 86, 96, 7, 33, 66, 32, 95, 71, 6, 28, 90, 79, 91, 24, 90, 41, 22, 58, 55, 54, 14, 8, 51, 79, 14, 22, 56, 34, 20, 99, 28, 6, 26, 40, 16, 26, 44, 77, 30, 8, 21, 86, 15, 62, 43, 4, 53, 37, 51, 81, 12, 39, 41, 79, 49, 76, 72, 79, 83, 64, 34, 79, 63, 35, 15, 23, 82, 5, 58, 14, 43, 13, 73, 17, 76, 62, 90, 20, 46, 48, 82, 36, 91, 18, 100, 15, 1, 39, 34, 49, 29, 32, 52, 7, 84, 52, 88, 37, 61, 77, 76, 65, 96, 99, 39, 37, 66, 80, 30, 23, 66, 39, 89, 63, 53, 67, 87, 60, 35, 57, 58, 3, 8, 83, 49, 22, 26, 65, 27, 75, 86, 10, 64, 60, 88, 65, 41, 36, 12, 95, 72, 83, 76, 56, 14, 86, 63, 83, 55, 2, 40, 50, 56, 16, 30, 81, 43, 15, 62, 42, 35, 43, 38, 52, 98, 0, 85, 91, 0, 59, 6, 12, 25, 88, 58, 39, 7, 5, 94, 13, 55, 13, 39, 58, 11, 61, 71, 38, 76, 91, 44, 98, 33, 21, 12, 84, 10, 47, 39, 92, 54, 2, 72, 58, 42, 8, 56, 32, 58, 65, 10, 80, 10, 94, 39, 6, 38, 55, 36, 94, 39, 73, 89, 40, 43, 95, 67, 94, 39, 6, 63, 46, 89, 42, 42, 64, 99, 50, 46, 57, 80, 9, 54, 81, 92, 14, 6, 67, 38, 19, 92, 11, 10, 60, 96, 2, 86, 8, 0, 20, 52, 10, 36, 94, 92, 97, 87, 92, 63, 56, 83, 96, 6, 97, 31, 49, 28, 44, 75, 91, 96, 90, 83, 2, 83, 89, 51, 100, 82, 76, 22, 5, 13, 3, 53, 20, 91, 7, 91, 78, 85, 56, 63, 48, 73, 91, 40, 79, 54, 37, 65, 8, 57, 50, 63, 81, 25, 32, 37, 76, 24, 89, 24, 34, 33, 45, 69, 43, 97, 10, 26, 32, 97, 80, 91, 54, 2, 18, 28, 68, 25, 12, 35, 5, 92, 88, 58, 36, 22, 30, 68, 91, 30, 82, 7, 54, 63, 7, 64, 9, 43, 81, 35, 92, 45, 60, 77, 3, 30, 71, 41, 45, 37, 30, 20, 17, 30, 59, 4, 57, 62, 36, 53, 69, 23, 100, 48, 45, 74, 48, 36, 37, 12, 2, 56, 30, 98, 37, 74, 46, 91, 11, 64, 91, 84, 21, 48, 66, 70, 39, 94, 46, 75, 83, 76, 71, 28, 3, 48, 7, 12, 47, 52, 91, 56, 22, 0, 73, 17, 100, 96, 81, 72, 29, 89, 5, 57, 67, 13, 22, 57, 64, 73, 62, 84, 65, 22, 56, 92, 63, 96, 32, 33, 39, 63, 16, 79, 46, 69, 69, 86, 35, 58, 65, 57, 85, 10, 7, 37, 65, 56, 38, 76, 90, 52, 36, 67, 20, 39, 73, 59, 60, 85, 16, 9, 19, 13, 2, 51, 73, 67, 41, 89, 10, 96, 65, 73, 6, 4, 18, 7, 47, 3, 62, 40, 30, 91, 99, 90, 30, 88, 8, 53, 4, 29, 64, 100, 80, 35, 48, 100, 3, 61, 24, 55, 59, 6, 59, 99, 38, 38, 59, 17, 5, 35, 42, 82, 56, 63, 69, 75, 77, 76, 24, 13, 46, 29, 95, 92, 57, 66, 42, 8, 60, 84, 81, 86, 41, 55, 75, 39, 78, 99, 42, 43, 51, 6, 73, 18, 44, 15, 4, 6, 76, 32, 47, 59, 96, 75, 14, 19, 27, 77, 13, 9, 8, 95, 100, 37, 23, 7, 6, 44, 78, 86, 89, 62, 7, 8, 77, 22, 72, 61, 54, 73, 69, 42, 86, 26, 66, 68, 41, 59, 45, 50, 25, 44, 28, 45, 8, 12, 19, 23, 14, 73, 22, 23, 30, 57, 0, 54, 37, 19, 89, 68, 68, 42, 3, 96, 91, 20, 35, 35, 94, 74, 52, 93, 52, 41, 16, 68, 43, 94, 9, 23, 26, 35, 70, 74, 68, 62, 66, 15, 70, 94, 17, 64, 35, 51, 10, 26, 31, 59, 44, 14, 64, 7, 75, 52, 83, 35, 29, 35, 83, 93, 74, 20, 73, 91, 75, 83, 3, 80, 92, 69, 10, 23, 42, 27, 48, 35, 23, 51, 68, 72, 68, 33, 58, 0, 48, 92, 56, 67, 82, 93, 55, 75, 94, 3, 48, 99, 62, 0, 90, 65, 48, 68, 79, 12, 34, 74, 66, 85, 1, 18, 87, 89, 4, 79, 78, 45, 25, 15, 59, 22, 30, 84, 43, 96, 44, 57, 56, 4, 87, 1, 38, 82, 49, 89, 5, 73, 70, 80, 66, 100, 65, 9, 25, 98, 39, 66, 28, 5, 71, 26, 73, 28, 36, 19, 23, 70, 4, 72, 40, 92, 84, 10, 0, 39, 75, 46, 68, 63, 50, 36, 45, 84, 7, 8, 98, 63, 63, 63, 85, 65, 73, 50, 46, 7, 66, 63, 50, 58, 28, 64, 0, 88, 13, 64, 95, 85, 21, 13, 0, 62, 67, 17, 3, 87, 85, 31, 40, 55, 26, 57, 59, 87, 4, 41, 4, 55, 16, 41, 34, 15, 82, 19, 99, 4, 38, 82, 8, 47, 81, 12, 90, 52, 93, 22, 32, 67, 13, 47, 10, 20, 6, 19, 26, 15, 26, 70, 61, 68, 7, 60, 92, 43, 54, 74, 62, 93, 30, 57, 52, 41, 41, 63, 56, 41, 30, 47, 89, 16, 34, 71, 96, 62, 96, 38, 52, 56, 54, 82, 98, 57, 57, 67, 39, 59, 28, 82, 3, 92, 2, 34, 71, 70, 27, 27, 35, 59, 96, 42, 45, 49, 23, 89, 94, 41, 59, 75, 33, 75, 80, 90, 24, 86, 13, 41, 69, 70, 23, 16, 14, 2, 19, 31, 64, 100, 75, 40, 57, 74, 38, 51, 9, 36, 24, 27, 93, 44, 34, 77, 73, 4, 3, 32, 52, 81, 19, 66, 42, 7, 72, 0, 82, 20, 40, 30, 11, 20, 26, 45, 54, 33, 67, 93, 63, 61, 15, 89, 26, 0, 3, 12, 41, 6, 13, 69, 0, 30, 75, 96, 17, 62, 50, 34, 3, 78, 62, 3, 83, 0, 85, 61, 32, 53, 8, 63, 22, 0, 0, 13, 9, 75, 35, 76, 30, 74, 95, 15, 32, 98, 19, 73, 31, 100, 94, 59, 52, 25, 74, 88, 50, 14, 43, 25, 50, 14, 0, 58, 22, 64, 51, 13, 32, 13, 31, 13, 83, 87, 68, 56, 4, 17, 2, 97, 50, 84, 96, 4, 21, 62, 89, 20, 94, 47, 47, 99, 76, 97, 86, 33, 68, 39, 21, 47, 7, 62, 41, 46, 59, 37, 52, 4, 67, 85, 28, 80, 53, 61, 33, 74, 36, 94, 84, 55, 68, 46, 9, 93, 51, 18, 66, 31, 99, 97, 83, 80, 21, 98, 6, 78, 95, 47, 77, 18, 95, 87, 6, 29, 66, 2, 29, 21, 99, 40, 72, 71, 21, 50, 59, 52, 68, 4, 37, 12, 38, 18, 41, 76, 63, 4, 84, 46, 93, 7, 36, 40, 83, 51, 95, 72, 3, 21, 93, 58, 5, 65, 22, 53, 86, 28, 73, 56, 4, 39, 77, 100, 90, 28, 24, 89, 63, 46, 74, 71, 0, 100, 37, 64, 58, 23, 5, 31, 80, 55, 54, 40, 89, 10, 39, 12, 73, 87, 3, 47, 83, 86, 31, 25, 12, 4, 73, 57, 74, 46, 14, 23, 50, 79, 56, 93, 83, 77, 56, 59, 24, 62, 19, 68, 31, 66, 41, 45, 57, 65, 46, 14, 86, 46, 4, 7, 2, 56, 89, 92, 70, 78, 99, 36, 83, 66, 85, 77, 48, 96, 2, 31, 95, 79, 49, 2, 24, 44, 33, 29, 68, 49, 52, 87, 54, 32, 7, 64, 73, 98, 97, 81, 85, 54, 44, 83, 49, 32, 44, 68, 27, 22, 37, 61, 54, 41, 37, 64, 11, 53, 62, 79, 47, 43, 53, 84, 18, 6, 18, 96, 81, 46, 51, 17, 14, 20, 23, 52, 66, 57, 29, 59, 43, 79, 29, 23, 81, 57, 59, 36, 67, 69, 37, 47, 50, 48, 71, 84, 94, 84, 26, 87, 17, 38, 58, 10, 76, 53, 1, 13, 41, 39, 28, 17, 70, 54, 67, 25, 98, 77, 11, 56, 70, 69, 30, 78, 78, 4, 82, 47, 78, 1, 27, 81, 83, 63, 24, 26, 46, 33, 88, 58, 54, 14, 70, 60, 24, 8, 90, 19, 3, 91, 66, 0, 14, 77, 66, 93, 26, 38, 13, 95, 9, 11, 52, 43, 12, 74, 44, 79, 32, 49, 81, 42, 32, 59, 26, 33, 14, 96, 100, 10, 46, 58, 22, 98, 34, 75, 95, 64, 11, 70, 68, 44, 80, 61, 67, 51, 21, 89, 48, 10, 12, 10, 18, 44, 32, 71, 95, 53, 38, 64, 82, 70, 15, 75, 40, 99, 96, 39, 41, 28, 94, 59, 75, 12, 62, 29, 25, 18, 54, 41, 28, 28, 0, 91, 59, 25, 14, 1, 37, 48, 100, 55, 31, 21, 84, 20, 76, 53, 95, 54, 64, 82, 32, 45, 97, 4, 77, 32, 30, 16, 22, 50, 91, 26, 61, 97, 44, 47, 22, 5, 92, 20, 3, 56, 39, 62, 3, 13, 83, 87, 16, 17, 13, 3, 15, 24, 71, 2, 75, 17, 53, 94, 15, 64, 15, 67, 17, 34, 62, 63, 74, 54, 86, 85, 56, 98, 70, 5, 45, 87, 87, 46, 59, 36, 49, 53, 22, 5, 99, 55, 59, 16, 2, 1, 80, 80, 24, 39, 65, 44, 17, 75, 80, 40, 12, 14, 33, 0, 98, 45, 77, 19, 93, 49, 1, 30, 22, 87, 39, 99, 76, 35, 70, 6, 71, 99, 48, 50]

average execution time for merge sort is: 9.977037100004964
average execution time for selection sort is: 388.49297600000864

time difference: 378.5159389000037
Selection sort takes 3793.87% more time than merge sort
"""