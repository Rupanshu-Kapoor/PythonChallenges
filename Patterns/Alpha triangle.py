"""
    date: 29-12-2023
    Alpha Triangle : https://www.codingninjas.com/studio/problems/alpha-triangle_6581429

Input: ‘N’ = 3

Output:
            C
            C B
            C B A
"""


#
def alphaTriangle(n: int) -> None:
    letter = 64 + n
    for i in range(n):

        for j in range(i + 1):
            print(chr(letter - j), end=" ")
        print("")


num = int(input("Enter \"N\" to print N Alpha Triangle: "))
alphaTriangle(num)
