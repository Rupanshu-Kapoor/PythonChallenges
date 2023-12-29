"""
    date: 29-12-2023
    Increasing Letter Triangle :https://www.codingninjas.com/studio/problems/increasing-letter-triangle_6581897?leftPanelTabValue=PROBLEM

Input: ‘N’ = 3

Output:
            A
            A B
            A B C

"""


def nLetterTriangle(n: int) -> None:

    letter = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(letter+j), end=" ")
        print("")


num = int(input("Enter \"N\" to print N Increasing Letter triangle: "))
nLetterTriangle(num)

