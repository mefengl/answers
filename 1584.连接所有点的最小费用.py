#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#

# @lc code=start

# # Kruskal
# class UnionFind:
#     def __init__(self, count: int) -> None:
#         self._count = count
#         self._parent = [i for i in range(count)]

#     def count(self) -> int:
#         return self._count

#     def __find(self, node: int) -> int:
#         if self._parent[node] != node:
#             self._parent[node] = self._find(self._parent[node])
#         return self._parent[node]

#     def union(self, node1: int, node2: int) -> bool:
#         root1 = self._find(node1)
#         root2 = self._find(node2)
#         if root1 == root2:
#             return False
#         self._parent[root2] = root1
#         self._count -= 1
#         return True

#     def is_connected(self, node1: int, node2: int) -> bool:
#         root1 = self._find(node1)
#         root2 = self._find(node2)
#         return root1 == root2


def manhattan_distance(point1: List[int], point2: List[int]) -> int:
    distances = []
    for start, end in zip(point1, point2):
        distances.append(abs(start - end))
    return sum(distances)


# class Solution:

#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         weight_edges = []
#         for i, point1 in enumerate(points):
#             for j, point2 in enumerate(points):
#                 # 跳过重复项和非边
#                 if i >= j:
#                     continue
#                 cost = manhattan_distance(point1, point2)
#                 # 点1，2的序号和cost
#                 weight_edges.append([i, j, cost])
#         # 按cost排序
#         weight_edges.sort(key=lambda x: x[2])

#         uf = UnionFind(len(points))
#         min_sumcost = 0
#         for start, end, cost in weight_edges:
#             if not uf.is_connected(start, end):
#                 uf.union(start, end)
#                 min_sumcost += cost
#         return min_sumcost if uf.count() == 1 else -1

# Prim
import queue


class Prim:
    def __init__(self, graph) -> None:
        self._graph = graph
        self._pq = queue.PriorityQueue()
        self._inMST = [False] * len(graph)
        self._sum_cost = 0

        self._inMST[0] = True
        self._cut(0)
        while not self._pq.empty():
            cost, _, to = self._pq.get()
            if self._inMST[to]:
                continue
            self._cut(to)
            self._inMST[to] = True
            self._sum_cost += cost

    def __cut(self, node: int) -> None:
        for edge in self._graph[node]:
            to = edge[2]
            if self._inMST[to]:
                continue
            self._pq.put(edge)

    def sum_cost(self) -> int:
        return self._sum_cost

    def all_connected(self) -> bool:
        return all(self._inMST)


def build_graph(points: List[List[int]]) -> List[List[int]]:
    len_points = len(points)
    graph = [[] for _ in range(len_points)]
    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points):
            if i >= j:
                continue
            cost = manhattan_distance(point1, point2)
            graph[i].append([cost, i, j])
            graph[j].append([cost, j, i])
    return graph


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = build_graph(points)
        prim = Prim(graph)
        return prim.sum_cost() if prim.all_connected() else -1


# @lc code=end
