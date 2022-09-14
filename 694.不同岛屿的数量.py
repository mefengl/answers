#
# @lc app=leetcode.cn id=694 lang=python3
#
# [694] 不同岛屿的数量
#

# @lc code=start
def dfs(grid, i, j, dir, path):
    row, col = len(grid), len(grid[0])
    if not (-1 < i < row and -1 < j < col):
        return
    if grid[i][j] != 1:
        return
    grid[i][j] = 0
    path.append(dir)
    dfs(grid, i - 1, j, 1, path)
    dfs(grid, i + 1, j, 2, path)
    dfs(grid, i, j - 1, 3, path)
    dfs(grid, i, j + 1, 4, path)
    path.append(-dir)


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    path = []
                    dfs(grid, i, j, 0, path)
                    islands.add(tuple(path))
        return len(islands)


# @lc code=end
