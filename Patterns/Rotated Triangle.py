"""
    date: 27-12-2023
    Reverse Star Triangle:https://www.codingninjas.com/studio/problems/rotated-triangle_6573688

    Input: ‘N’ = 3
    Output:
            *
            **
            ***
            **
            *
"""


def rotatedTriangle(n: int) -> None:
    for i in range(1,n+1):
        string = i * "*"
        print(string)

    for i in range(n-1,0,-1):
        string = i * "*"
        print(string)


num = int(input("Enter \"N\" to print N star Triangle: "))
rotatedTriangle(num)

