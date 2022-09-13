#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
def dfs(grid, i, j):
    if not (-1 < i < len(grid) and -1 < j < len(grid[0])):
        return
    if grid[i][j] != 0:
        return
    grid[i][j] = 1
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # 淹没 左，右 陆地
        for i in range(row):
            dfs(grid, i, 0)
            dfs(grid, i, col - 1)
        # 淹没 上，下 陆地
        for i in range(col):
            dfs(grid, 0, i)
            dfs(grid, row - 1, i)
        # 淹没各个岛屿
        count = 0
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if grid[i][j] == 0:
                    dfs(grid, i, j)
                    count += 1
        return count


# @lc code=end
