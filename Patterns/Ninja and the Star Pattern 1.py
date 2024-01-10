"""
    date: 29-12-2023
    Ninja and the Star Pattern1 : https://www.codingninjas.com/studio/problems/ninja-and-the-star-pattern-i_6581920

    Runtime: Better than 100% users :*

Input: ‘N’ = 4

Output:
            ****
            *  *
            *  *
            ****
"""


#
def getStarPattern(n: int) -> None:

    for i in range(n):
        if i == 0 or i == n-1:
            string = n*"* "
        else:
            string = "* " + (n-2)*"  "+"*"
        print(string)


num = int(input("Enter \"N\" to print N*N Star Pattern: "))
getStarPattern(num)
