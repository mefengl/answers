#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            def notvaild(row, col):
                for offset in range(1, row + 1):
                    if board[row - offset][col] == "Q":
                        return True
                for offset in range(1, col + 1):
                    if row - offset < 0:
                        break
                    if board[row - offset][col - offset] == "Q":
                        return True
                for offset in range(1, n - col):
                    if row - offset < 0:
                        break
                    if board[row - offset][col + offset] == "Q":
                        return True
                return False

            if row == n:
                temp = ["".join(x) for x in board]
                result.append(temp)
                return
            for col in range(n):
                if notvaild(row, col):
                    continue
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

        backtrack(0)
        return result

        # @lc code=end
