"""
    date = 27-12-2023
    N/2 Forest: https://www.codingninjas.com/studio/problems/n-2-forest_6570178

    Input = 3
    Output:
            *
            * *
            * * *
"""


def nForest(n: int) -> None:

    for i in range(1,n+1):
        for j in range(0,i):
            print("*", end=" ")
        print("")


num = int(input("Enter \"N\" to print N/2 forest: "))
nForest(num)