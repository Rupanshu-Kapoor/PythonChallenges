"""
    date: 27-12-2023
    Seeding: https://www.codingninjas.com/studio/problems/seeding_6581892

    Input: ‘N’ = 3

    Output:
    * * *
    * *
    *
"""


def seeding(n: int) -> None:

    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print("")


num = int(input("Enter \"N\" to print N Seeding: "))
seeding(num)

