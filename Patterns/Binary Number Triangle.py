"""
    date: 29-12-2023
    Binary Number Triangle:https://www.codingninjas.com/studio/problems/binary-number-triangle_6581890

Input: ‘N’ = 3

Output:
        1
        0 1
        1 0 1
"""


def nBinaryTriangle(n: int) -> None:
    # initially declared boool = True to first print "1"
    boool = True
    for i in range(1,n+1):
        # stored last bool value to alter boolean value at every new row
        last_bool = boool
        for j in range(i):
            print(int(boool),end=" ")
            # altered boolean value after every number gets printed
            boool = not boool
        print("")
        boool = not last_bool


num = int(input("Enter \"N\" to print N Binary Number Triangle: "))
nBinaryTriangle(num)

