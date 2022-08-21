#
# @lc app=leetcode.cn id=1135 lang=python3
#
# [1135] 最低成本联通所有城市
#

# @lc code=start
class UnionFind:
    def __init__(self, count: int) -> None:
        self.__count = count
        self.__parent = [i for i in range(count)]

    def count(self) -> int:
        return self.__count

    def __find(self, node: int) -> int:
        if self.__parent[node] != node:
            self.__parent[node] = self.__find(self.__parent[node])
        return self.__parent[node]

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.__find(node1)
        root2 = self.__find(node2)
        if root1 == root2:
            return False
        self.__parent[root2] = root1
        self.__count -= 1
        return True

    def is_connected(self, node1: int, node2: int) -> bool:
        root1 = self.__find(node1)
        root2 = self.__find(node2)
        return root1 == root2


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        # 按sort排序
        connections.sort(key=lambda x: x[2])
        min_cost = 0
        for start, end, cost in connections:
            start -= 1
            end -= 1
            if not uf.is_connected(start, end):
                uf.union(start, end)
                min_cost += cost
        return min_cost if uf.count() == 1 else -1


# @lc code=end
