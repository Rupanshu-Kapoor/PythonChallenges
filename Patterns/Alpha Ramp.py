"""
    date: 29-12-2023
    Alpha Ramp :https://www.codingninjas.com/studio/problems/alpha-ramp_6581888

Input: ‘N’ = 3

Output:
            A
            B B
            C C C
"""


def alphaRamp(n: int) -> None:

    letter = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(letter), end=" ")
        print("")
        letter += 1


num = int(input("Enter \"N\" to print N Alpha Hill: "))
alphaRamp(num)

