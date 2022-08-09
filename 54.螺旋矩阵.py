#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m-1, 0, n-1
        res = []
        while top <= bottom and left <= right:
            # >
            if top <= bottom:
                for col in range(left, right+1):
                    res.append(matrix[top][col])
                top += 1
            # \/
            if left<=right:
                for row in range(top, bottom+1):
                    res.append(matrix[row][right])
                right -= 1
            # <
            if top <= bottom:
                for col in range(right, left-1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            # /\
            if left<=right:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res


# @lc code=end
