"""
    date: 27-12-2023
    Seeding: https://www.codingninjas.com/studio/problems/reverse-number-triangle_6581889

    Input: ‘N’ = 3
    Output:
        1 2 3
        1 2
        1
"""


def nNumberTriangle(n: int) -> None:

    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("")


num = int(input("Enter \"N\" to print N Seeding: "))
nNumberTriangle(num)

