#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        len_row = len(matrix)
        len_col = len(matrix[0])
        # 左上，上，右上
        directions = [[-1, -1], [-1, 0], [-1, 1]]
        for i in range(len_row):
            # 第一行不会有任何cost更新，跳过
            if i == 0:
                continue
            for j in range(len_col):
                cost = []
                for di, dj in directions:
                    next_i = i + di
                    next_j = j + dj
                    # 如果越界
                    if not (0 <= next_i < len_row and 0 <= next_j < len_col):
                        continue
                    cost.append(matrix[i][j] + matrix[next_i][next_j])
                if len(cost) == 0:
                    continue
                matrix[i][j] = min(cost)
        return min(matrix[-1])


# @lc code=end
