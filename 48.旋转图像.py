#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenmatrix = len(matrix)
        # 逆转
        for x in range(lenmatrix):
            for y in range(x+1, lenmatrix):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        # 行翻转
        for row in matrix:
            left, right = 0, lenmatrix-1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
# @lc code=end
