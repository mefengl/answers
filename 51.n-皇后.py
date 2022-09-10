#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(queens: List[List[int]], xy_sub: List[int], xy_sum: List[int]) -> None:
            x = len(queens)
            if x == n:
                res.append(queens)
                return
            for y in range(n):
                # 行列值的加减结果能确定唯一的斜线
                if (y in queens) or (x - y in xy_sub) or (x + y in xy_sum):
                    continue
                else:
                    dfs(queens + [y], xy_sub + [x - y], xy_sum + [x + y])

        dfs([], [], [])
        return [
            ["." * i + "Q" + "." * (n - i - 1) for i in single_res]
            for single_res in res
        ]


# @lc code=end
