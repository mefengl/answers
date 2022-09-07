#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#


# @lc code=start
# Dijkstra
import queue


# BFS
def build_graph(paths: List[List[int]]):
    res = collections.defaultdict(list)
    for beg, end, cost in paths:
        res[beg].append((cost, end))
    return res


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = build_graph(flights)
        pq = queue.PriorityQueue()
        # 用于剪枝
        visited_times = [0] * n
        pq.put((0, k + 1, src))
        while not pq.empty():
            cost, visited, end = pq.get()
            if end == dst:
                return cost
            if visited_times[end] >= visited:
                continue
            visited_times[end] = visited
            for cur_cost, cur_end in graph[end]:
                pq.put((cur_cost + cost, visited - 1, cur_end))
        return -1


# @lc code=end
