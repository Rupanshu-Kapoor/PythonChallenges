'''
    date: 27-12-2023
    N triangle: https://www.codingninjas.com/studio/problems/n-triangles_6573689?leftPanelTabValue=PROBLEM
    Input: ‘N’ = 3

    Output:
    1
    1 2
    1 2 3
'''


def nTriangle(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")


num = int(input("Enter \"N\" to print N Triangle: "))
nTriangle(num)
