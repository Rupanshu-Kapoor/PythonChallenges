"""
    date: 27-12-2023
    triangle: https://www.codingninjas.com/studio/problems/triangle_6573690

    Input: ‘N’ = 3

    Output:
    1
    2 2
    3 3 3
"""


def triangle(n: int) -> None:
    # Write your solution here.
    pass
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print("")


num = int(input("Enter \"N\" to print N Triangle: "))
triangle(num)
