#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class UnionFind:
    def __init__(self, count: int):
        self.count = count
        self._parent = [i for i in range(count)]

    def union(self, p, q):
        root_p = self._find(p)
        root_q = self._find(q)
        if root_p == root_q:
            return
        else:
            self._parent[root_q] = root_p
            self.count -= 1

    def __find(self, node):
        if self._parent[node] != node:
            # 这里find的递归需要深入到parent，否则会无限递归
            self._parent[node] = self._find(self._parent[node])
        return self._parent[node]

    def __parent(self, node):
        return self._parent[node]

    def is_connected(self, p, q):
        root_p = self._find(p)
        root_q = self._find(q)
        return root_p == root_q


BIG_O = "O"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        len_row = len(board)
        len_col = len(board[0])
        if len_row == 0:
            return None
        union_find = UnionFind(len_row * len_col + 1)
        dummy = len_row * len_col
        for row in range(len_row):
            if board[row][0] == BIG_O:
                union_find.union(dummy, row * len_col + 0)
            if board[row][len_col - 1] == BIG_O:
                union_find.union(dummy, row * len_col + len_col - 1)
        for col in range(len_col):
            if board[0][col] == BIG_O:
                union_find.union(dummy, 0 * len_col + col)
            if board[len_row - 1][col] == BIG_O:
                union_find.union(dummy, (len_row - 1) * len_col + col)

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for row in range(1, len_row - 1):
            for col in range(1, len_col - 1):
                if board[row][col] == BIG_O:
                    # 遍历范围决定了不会越界
                    for row_d, col_d in directions:
                        next_row = row + row_d
                        next_col = col + col_d
                        # 没有这个if，会将X与O相连，应该将两个O相邻相连
                        if board[next_row][next_col] == BIG_O:
                            union_find.union(
                                row * len_col + col, next_row * len_col + next_col
                            )

        for row in range(1, len_row - 1):
            for col in range(1, len_col - 1):
                if not union_find.is_connected(row * len_col + col, dummy):
                    board[row][col] = "X"


# @lc code=end
