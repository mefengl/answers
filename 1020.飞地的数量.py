#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
def dfs(grid, i, j):
    if not (-1 < i < len(grid) and -1 < j < len(grid[0])):
        return
    if grid[i][j] != 1:
        return
    grid[i][j] = 0
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for i in range(row):
            dfs(grid, i, 0)
            dfs(grid, i, col - 1)
        for j in range(col):
            dfs(grid, 0, j)
            dfs(grid, row - 1, j)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 1
        return count


# @lc code=end
