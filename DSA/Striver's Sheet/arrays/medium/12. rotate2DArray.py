"""
Rotate Image: https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Optimal Approach: First we transpose the matrix and then reverse every row
        :TC: O( N/2* N/2) + O(N * N/2)
        :SC: O(1)
        :param matrix:
        :return:
        """
        size = len(matrix)

        # transposing matrix
        # while transposing, diagonal remains same, and all othe    r elements interchange rows and cols
        # TC O(N/2 * N/2)
        for row in range(size):
            for col in range(row+1, size):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # reversing each row of transposed matrix
        # TC: O(N * N/2)
        for row in range(size):
            start = 0
            end = size-1
            while start <= end:
                matrix[row][start], matrix[row][end] = matrix[row][end], matrix[row][start]
                start += 1
                end -= 1

    def rotateBF(self, matrix: list[list[int]]) -> None:
        """
        Brute Force: We take every col and put it as row in new matrix
        :TC: O(N * N)
        :SC: O(N * N)
        :param matrix:
        :return:
        """
        new_matrix = []
        cur_row = []
        size = len(matrix)
        for col in range(size):
            for row in range(size - 1, -1, -1):
                cur_row.append(matrix[row][col])
            new_matrix.append(cur_row)
            cur_row = []
        matrix[:] = new_matrix


a = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(a)
obj = Solution()
obj.rotate(a)
print(a)
