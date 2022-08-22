#
# @lc app=leetcode.cn id=1135 lang=python3
#
# [1135] 最低成本联通所有城市
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


# class Solution:
#     def minimumCost(self, n: int, connections: List[List[int]]) -> int:
#         uf = UnionFind(n)
#         # 按sort排序
#         connections.sort(key=lambda x: x[2])
#         min_cost = 0
#         for start, end, cost in connections:
#             start -= 1
#             end -= 1
#             if not uf.is_connected(start, end):
#                 uf.union(start, end)
#                 min_cost += cost
#         return min_cost if uf.count() == 1 else -1

# Prim
import queue


class Prim:
    def __init__(self, graph: List[List[int]]):
        self._graph = graph
        self._inMST = [False] * len(graph)
        self._pq = queue.PriorityQueue()
        self._cost_sum = 0

        self._inMST[0] = True
        self._cut(0)
        while not self._pq.empty():
            cost, _, to = self._pq.get()
            if self._inMST[to]:
                continue
            self._cut(to)
            self._inMST[to] = True
            self._cost_sum += cost

    def __cut(self, node: int) -> None:
        for edge in self._graph[node]:
            to = edge[2]
            if self._inMST[to]:
                continue
            self._pq.put(edge)

    def all_connected(self) -> bool:
        return all(self._inMST)

    def cost_sum(self) -> int:
        return self._cost_sum


def build_graph(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph = [[] for _ in range(n)]
    for start, end, cost in connections:
        start -= 1
        end -= 1
        graph[start].append([cost, start, end])
        graph[end].append([cost, end, start])
    return graph


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = build_graph(n, connections)
        prim = Prim(graph)
        return prim.cost_sum() if prim.all_connected() else -1


# @lc code=end
