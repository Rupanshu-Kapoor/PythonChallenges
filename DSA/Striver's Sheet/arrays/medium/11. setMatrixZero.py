"""
Set Matrix Zeroes:https://leetcode.com/problems/set-matrix-zeroes/description/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
import numpy as np


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero.append((i, j))

        for i in zero:
            matrix[i[0]] = [0] * len(matrix[i[0]])
        print(zero)

        return matrix

    def setZeroesNP(self, matrix: list[list[int]]) -> None:
        """
        using Numpy arrays
        :param matrix:
        :return:
        """
        matrix_temp = np.array(matrix)
        zero = np.array(np.where(matrix_temp == 0))

        for row, col in zip(zero[0], zero[1]):
            matrix_temp[row] = 0
            matrix_temp[:, col] = 0

        matrix[:] = matrix_temp.tolist()

    def setZeroesBT(self, matrix):
        row = [0] * len(matrix)
        col = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i], col[j] = 1, 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0


    def setZeroesOP(self, matrix):

        col0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = -1

                    if j == 0:
                        col0 = -1
                    else:
                        matrix[0][j] = -1
        print(matrix)
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):

                if matrix[i][0] == -1 or matrix[0][j] == -1:
                    matrix[i][j] = 0

        for i in range(len(matrix)):
            if matrix[i][0] == -1:
                matrix[i] = [0] * len(matrix[i])

        for j in range(1,len(matrix[0])):
            if matrix[0][j] == -1:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        if col0 == -1:
            for i in range(len(matrix)):
                matrix[i][0] = 0


    def zeroMatrix(self, matrix):
        # int row[n] = {0}; --> matrix[..][0]
        # int col[m] = {0}; --> matrix[0][..]
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1
        # step 1: Traverse the matrix and
        # mark 1st row & col accordingly:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark i-th row:
                    matrix[i][0] = 0

                    # mark j-th column:
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    # check for col & row:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        #step 3: Finally mark the 1st col & then 1st row:
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0






a = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
obj = Solution()
# (obj.setZeroesOP(a))
# (obj.setZeroesBT(a))
obj.zeroMatrix(a)
print(a)
