"""
    date: 29-12-2023
    Reverse Letter Triangle :https://www.codingninjas.com/studio/problems/reverse-letter-triangle_6581906
Input: ‘N’ = 3

Output:
            A B C
            A B
            A
"""


def nLetterTriangle(n: int) -> None:

    letter = 65
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(letter+j), end=" ")
        print("")


num = int(input("Enter \"N\" to print N Reverse Letter Triangle: "))
nLetterTriangle(num)

