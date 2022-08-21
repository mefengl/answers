#
# @lc app=leetcode.cn id=1135 lang=python3
#
# [1135] 最低成本联通所有城市
#

# @lc code=start

# # Kruskal
# class UnionFind:
#     def __init__(self, count: int) -> None:
#         self.__count = count
#         self.__parent = [i for i in range(count)]

#     def count(self) -> int:
#         return self.__count

#     def __find(self, node: int) -> int:
#         if self.__parent[node] != node:
#             self.__parent[node] = self.__find(self.__parent[node])
#         return self.__parent[node]

#     def union(self, node1: int, node2: int) -> bool:
#         root1 = self.__find(node1)
#         root2 = self.__find(node2)
#         if root1 == root2:
#             return False
#         self.__parent[root2] = root1
#         self.__count -= 1
#         return True

#     def is_connected(self, node1: int, node2: int) -> bool:
#         root1 = self.__find(node1)
#         root2 = self.__find(node2)
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
        self.__graph = graph
        self.__inMST = [False] * len(graph)
        self.__pq = queue.PriorityQueue()
        self.__cost_sum = 0

        self.__inMST[0] = True
        self.__cut(0)
        while not self.__pq.empty():
            cost, _, to = self.__pq.get()
            if self.__inMST[to]:
                continue
            self.__cut(to)
            self.__inMST[to] = True
            self.__cost_sum += cost

    def __cut(self, node: int) -> None:
        for edge in self.__graph[node]:
            to = edge[2]
            if self.__inMST[to]:
                continue
            self.__pq.put(edge)

    def all_connected(self) -> bool:
        return all(self.__inMST)

    def cost_sum(self) -> int:
        return self.__cost_sum


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
