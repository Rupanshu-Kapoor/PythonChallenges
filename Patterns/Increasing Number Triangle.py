"""
    date: 29-12-2023
    Increasing Number Triangle :https://www.codingninjas.com/studio/problems/increasing-number-triangle_6581893

Input: ‘N’ = 3

Output:
            1
            2 3
            4 5 6
"""


def nNumberTriangle(n: int) -> None:

    number = 1
    for i in range(n):
        for j in range(i+1):
            print(number,end=" ")
            number += 1
        print("")

num = int(input("Enter \"N\" to print N Increasing Number Triangle: "))
nNumberTriangle(num)

