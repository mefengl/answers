#
# @lc app=leetcode.cn id=323 lang=python3
#
# [323] 无向图中连通分量的数目
#

# @lc code=start
class UnionFind:
    def __init__(self, count: int):
        self.__count = count
        self.__parent = [i for i in range(count)]

    def union(self, p: int, q: int):
        root_p = self.__find(p)
        root_q = self.__find(q)
        if root_p == root_q:
            return
        # 合并两棵树
        self.__parent[root_q] = root_p
        self.__count -= 1

    def is_connected(self, p: int, q: int) -> bool:
        root_p = self.__find(p)
        root_q = self.__find(q)
        return root_p == root_q

    def __find(self, node: int):
        # 高效版
        if self.__parent[node] != node:
            self.__parent[node] = self.__find(self.__parent[node])
        # 这里不能返回node了，因为迭代只是改变了node的parent
        return self.__parent[node]
        # # 普通版
        # while self.__parent[node] != node:
        #     node = self.__parent[node]
        # return node

    def count(self) -> int:
        return self.__count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for p, q in edges:
            union_find.union(p, q)
        return union_find.count()


# @lc code=end
