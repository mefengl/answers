#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
from typing import List
import queue


def dijkstra(start: int, graph: List[List[int]]) -> List[int]:
    cost_to = [float("inf")] * len(graph)
    cost_to[start] = 0

    pq = queue.PriorityQueue()
    pq.put([0, start])
    while not pq.empty():
        cur_cost, start = pq.get()
        if cur_cost > cost_to[start]:
            continue
        for next_node in graph[start]:
            cost, start, next = next_node
            cost_to_next = cur_cost + cost
            # 通过更远路径到达相同节点毫无意义
            if cost_to_next >= cost_to[next]:
                continue
            cost_to[next] = cost_to_next
            pq.put([cost_to_next, next])
    return cost_to


def build_graph(n: int, times: List[List[int]]) -> List[List[int]]:
    graph = [[] for _ in range(n)]
    for start, end, cost in times:
        start -= 1
        end -= 1
        graph[start].append([cost, start, end])
        # 此题是单向的
        # graph[end].append([cost,end,start])
    return graph


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = build_graph(n, times)
        cost_to = dijkstra(k - 1, graph)
        res = max(cost_to)
        print(cost_to)
        return -1 if res == float("inf") else res


# @lc code=end
