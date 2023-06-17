#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
def dfs(grid, i, j):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        return
    # 只修改当前岛屿
    if grid[i][j] != "1":
        return
    grid[i][j] = "0"
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "1":
                    continue
                dfs(grid, i, j)
                count += 1
        return count


# @lc code=end
