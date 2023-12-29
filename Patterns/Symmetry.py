"""
    date: 29-12-2023
    Symmetry : https://www.codingninjas.com/studio/problems/alpha-triangle_6581429

    Runtime: Better than 100% users :*

Input: ‘N’ = 3

Output:
            *         *
            * *     * *
            * * * * * *
            * *     * *
            *         *
"""


#
def symmetry(n: int) -> None:
    max_width = 2*n
    string = ""
    for i in range(n):
        string = (i + 1) * "* "
        print(string.ljust(max_width), end="")
        print(string.rjust(max_width))
    for i in range(n-1,0,-1):
        string = i*"* "
        print(string.ljust(max_width), end="")
        print(string.rjust(max_width))


num = int(input("Enter \"N\" to print N Symmetry: "))
symmetry(num)
