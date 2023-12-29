"""
    date: 29-12-2023
    Alpha Hill :https://www.codingninjas.com/studio/problems/alpha-hill_6581921

Input: ‘N’ = 3

Output:
            A
          A B A
        A B C B A
"""


#
def alphaHill(n: int) -> None:

    letter = 65
    max_width = 2 * (2 * n - 1)
    for i in range(n):
        string = ""

        for j in range(i+1):
            string += chr(letter+j) + " "
        for j in range(i, 0, -1):
            string += chr(letter+j-1) + " "
        print(string.center(max_width))


num = int(input("Enter \"N\" to print N Alpha Hill: "))
alphaHill(num)

