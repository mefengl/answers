#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
from typing import List


# @lc code=start
def back_track(board, i, j):
    m = n = 9
    if j == n:
        return back_track(board, i + 1, 0)
    if i == m:
        return True
    if board[i][j] != ".":
        # 跳过
        return back_track(board, i, j + 1)
    # '1'-'9'
    for idx in range(1, 10):
        ch = str(idx)
        if not is_valid(board, i, j, ch):
            continue
        board[i][j] = ch
        # 只有无结果才继续遍历下去
        if back_track(board, i, j + 1):
            return True
        board[i][j] = "."
    return False


def is_valid(board, row, col, ch):
    # 检查行和列
    for i in range(9):
        if board[row][i] == ch or board[i][col] == ch:
            return False
    # 检查小9格
    # 0,1,2->0; 3,4,5->3; 6,7,8->6
    start_row, start_col = row // 3 * 3, col // 3 * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == ch:
                return False
    return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        back_track(board, 0, 0)


# if __name__ == "__main__":
#     Solution().solveSudoku(
#         [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"],
#         ]
#     )

# @lc code=end
