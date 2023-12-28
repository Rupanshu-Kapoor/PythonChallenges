'''
    date: 27-12-2023
    N-forest : https://www.codingninjas.com/studio/problems/n-forest_6570177

    input = 3
    output= * * *
            * * *
            * * *
'''


def nForest(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("")


number = int(input("Enter a number \"N\" to print N*N size forest:"))
nForest(number)
