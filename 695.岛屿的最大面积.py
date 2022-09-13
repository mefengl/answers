#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
def dfs(grid, i, j) -> int:
    if not (-1 < i < len(grid) and -1 < j < len(grid[0])):
        return 0
    if grid[i][j] != 1:
        return 0
    grid[i][j] = 0
    return (
        1
        + dfs(grid, i - 1, j)
        + dfs(grid, i + 1, j)
        + dfs(grid, i, j - 1)
        + dfs(grid, i, j + 1)
    )


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, dfs(grid, i, j))
        return area


# @lc code=end
