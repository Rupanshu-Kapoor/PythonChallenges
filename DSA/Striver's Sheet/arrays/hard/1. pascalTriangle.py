"""
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2
Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generateBF(self, numRows: int) -> list[list[int]]:
        """
        Brute force approach to generate complete pascal triangle based.
        approach: each element is sum of two directly above numbers
        :param numRows:
        :return:
        """
        pas = []
        # iterate to have numRows
        for i in range(numRows):
            row = []
            # iterate to generate each row
            for j in range(0, i + 1):
                # if its either first or last element, insert 1
                if j == 0 or j == i:
                    row.append(1)
                # if not, then take the sum of two directly above numbers
                else:
                    plus = pas[-1][j - 1] + pas[-1][j]
                    row.append(plus)
            pas.append(row)
        return pas

    def generateOP(self, numRows: int) -> list[list[int]]:
        """
        Optimal approach to generate pascal triangle.
        :param numRows:
        :return:
        """
        # 1st element will always be 1, initializing ans list with [1]
        ans = [[1]]
        # iterate till numRows
        for i in range(1, numRows):
            # 1st element of each row will always be 1
            row = [1]
            # generating each element of the rows
            for j in range(i):
                ele = row[-1] * (i - j) / (j + 1)
                row.append(int(ele))    # append every element to form a row
            ans.append(row)     # append every row in ans
        return ans

    def generateElement(self, row: int, col: int) -> int:
        """
        Generate a particular element of pascal triangle given row and col.
        :Institution: Every element can be produced by (n-1) C (r-1)
        :param row: Row number of element
        :param col: Column number of element(1-index)
        :return: element at row and col
        """
        ans = 1
        for i in range(col - 1):
            ans = ans * (row - 1) / (i + 1)
            row -= 1
        return int(ans)

    def generateRow(self, n: int) -> list[int]:
        """
        Generate the complete nth row of pascal triangle:

        :param n: nth row to generate
        :return: nth row of pascal triangle
        """
        ans = [1]
        row = n
        for i in range(1, row):
            ele = ans[-1] * (n - i) / i
            ans.append(int(ele))
        return ans


obj = Solution()
print(obj.generateElement(5, 3))
print(obj.generateRow(5))
print(obj.generateBF(7))
print(obj.generateOP(7))
