"""
    date: 27-12-2023
    Star Diamond: https://www.codingninjas.com/studio/problems/star-diamond_6573686

    Input: ‘N’ = 3
    Output:
              *
             ***
            *****
            *****
             ***
              *
"""


def nStarDiamond(n: int) -> None:
    for i in range(0,n):
        max_width = 2*(n-1)+1
        odd_num = 2*i+1
        string = odd_num * "*"
        print(string.center(max_width, " "))
    for i in range(n-1,-1,-1):
        max_width = 2*(n-1)+1
        odd_num = 2*i+1
        string = odd_num * "*"
        print(string.center(max_width, " "))


num = int(input("Enter \"N\" to print N star Triangle: "))
nStarDiamond(num)

