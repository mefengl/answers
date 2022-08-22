#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] 概率最大的路径
#

# @lc code=start
import queue


def build_graph(
    n: int, edges: List[List[int]], succProb: List[float]
) -> List[List[int]]:
    graph = [[] for _ in range(n)]
    for [start, end], prob in zip(edges, succProb):
        # 无向边
        graph[start].append([prob, start, end])
        graph[end].append([prob, end, start])
    return graph


def dijkstra(start: int, graph: List[List[int]]) -> List[int]:
    cost_to = [float("-inf")] * len(graph)

    pq = queue.PriorityQueue()
    # 乘法里的0是1
    cost_to[start] = 1
    pq.put([1, start])
    while not pq.empty():
        cur_cost, start = pq.get()
        # 负数是为了优先队列排序，这里需要归正
        cur_cost = abs(cur_cost)
        if cur_cost < cost_to[start]:
            continue
        for next_cost, _, next in graph[start]:
            cost_to_next = cur_cost * next_cost
            if cost_to_next <= cost_to[next]:
                continue
            cost_to[next] = cost_to_next
            pq.put([-cost_to_next, next])
    return cost_to


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = build_graph(n, edges, succProb)
        cost_to = dijkstra(start, graph)
        return 0 if cost_to[end] == float("-inf") else cost_to[end]


# @lc code=end
