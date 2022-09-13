#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#

# @lc code=start
def dfs(grid, i, j):
    if not (-1 < i < len(grid) and -1 < j < len(grid[0])):
        return
    if not grid[i][j] == 1:
        return
    grid[i][j] = 0
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid1), len(grid1[0])
        for i in range(row):
            for j in range(col):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(grid2, i, j)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:
                    dfs(grid2, i, j)
                    count += 1
        return count


# @lc code=end
