"""
    date: 27-12-2023
    Reverse Star Triangle:https://www.codingninjas.com/studio/problems/binary-number-triangle_6581890

Input: ‘N’ = 3

Output:
        1
        0 1
        1 0 1
"""

def nBinaryTriangle(n: int) -> None:

    boool = False
    for i in range(1,n+1):
        for j in range(i):
            boool = not(boool)
            print(int(boool),end="")
        print("")

# num = int(input("Enter \"N\" to print N star Triangle: "))
nBinaryTriangle(3)

