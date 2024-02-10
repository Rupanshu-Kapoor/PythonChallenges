"""
Spiral Matrix: https://leetcode.com/problems/spiral-matrix/description/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top = left = 0
        bottom = len(matrix) - 1  # last index of the row
        right = len(matrix[0]) - 1  # last index of the column
        ans = []

        while top <= bottom and left <= right:

            # for the top most row
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # for right column
            for j in range(top, bottom + 1):
                ans.append(matrix[j][right])
            right -= 1

            # for bottom row
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    ans.append(matrix[bottom][k])
                bottom -= 1

            # for left column
            if left <= right:
                for m in range(bottom, top - 1, -1):
                    ans.append(matrix[m][left])
                left += 1
        return ans


a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
# print(a)
obj = Solution()
print(obj.spiralOrder(a))
