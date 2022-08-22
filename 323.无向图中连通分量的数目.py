#
# @lc app=leetcode.cn id=323 lang=python3
#
# [323] 无向图中连通分量的数目
#

# @lc code=start
class UnionFind:
    def __init__(self, count: int):
        self._count = count
        self._parent = [i for i in range(count)]

    def union(self, p: int, q: int):
        root_p = self._find(p)
        root_q = self._find(q)
        if root_p == root_q:
            return
        # 合并两棵树
        self._parent[root_q] = root_p
        self._count -= 1

    def is_connected(self, p: int, q: int) -> bool:
        root_p = self._find(p)
        root_q = self._find(q)
        return root_p == root_q

    def __find(self, node: int):
        # 高效版
        if self._parent[node] != node:
            self._parent[node] = self._find(self._parent[node])
        # 这里不能返回node了，因为迭代只是改变了node的parent
        return self._parent[node]
        # # 普通版
        # while self._parent[node] != node:
        #     node = self._parent[node]
        # return node

    def count(self) -> int:
        return self._count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for p, q in edges:
            union_find.union(p, q)
        return union_find.count()


# @lc code=end
