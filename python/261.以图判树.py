#
# @lc app=leetcode.cn id=261 lang=python3
#
# [261] 以图判树
#

# @lc code=start
class UnionFind:
    def __init__(self, count: int) -> None:
        self._count = count
        self._parent = [i for i in range(count)]

    def __find(self, node: int) -> int:
        if self._parent[node] != node:
            self._parent[node] = self._find(self._parent[node])
        return self._parent[node]

    def union(self, node1, node2) -> bool:
        roo1 = self._find(node1)
        roo2 = self._find(node2)
        if roo1 == roo2:
            # 表示早已连接
            return False
        self._parent[roo2] = roo1
        self._count -= 1
        return True

    def is_connected(self, node1: int, node2: int) -> bool:
        roo1 = self._find(node1)
        roo2 = self._find(node2)
        return roo1 == roo2

    def count(self) -> int:
        return self._count


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for start, end in edges:
            # 如果连接中发现早已连接，返回False
            if not uf.union(start, end):
                return False
        # 不能直接return True，因为不能确定是否只有一棵树
        # return True
        return True if uf.count() == 1 else False


# @lc code=end
