#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
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
    def manhattan_distance(self, point1: List[int], point2: List[int]) -> int:
        distances = []
        for start, end in zip(point1, point2):
            distances.append(abs(start - end))
        return sum(distances)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weight_edges = []
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                # 跳过重复项和非边
                if i >= j:
                    continue
                cost = self.manhattan_distance(point1, point2)
                # 点1，2的序号和cost
                weight_edges.append([i, j, cost])
        # 按cost排序
        weight_edges.sort(key=lambda x: x[2])

        uf = UnionFind(len(points))
        min_sumcost = 0
        for start, end, cost in weight_edges:
            if not uf.is_connected(start, end):
                uf.union(start, end)
                min_sumcost += cost
        return min_sumcost if uf.count() == 1 else -1


# @lc code=end
