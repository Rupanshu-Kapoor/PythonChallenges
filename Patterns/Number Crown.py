"""
    date: 29-12-2023
    Number Crown :https://www.codingninjas.com/studio/problems/number-crown_6581894

Input: ‘N’ = 3

Output:
            1         1
            1 2     2 1
            1 2 3 3 2 1
"""


def numberCrown(n: int) -> None:

    max_width = 2*n
    left_string = right_string= ""
    for i in range(n):
        for j in range(i+1):
            left_string = left_string+str(j+1)+" "

        for j in range(i+1,0,-1):
            right_string = right_string+str(j)+" "

        print(left_string.ljust(max_width), end="")
        print(right_string.center(max_width))
        left_string = right_string = ""


num = int(input("Enter \"N\" to print N Number Crown: "))
numberCrown(num)

