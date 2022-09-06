#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#


# @lc code=start
# Dijkstra
import queue


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
        cost_to = [float("inf")] * n
        transited_to = [float("inf")] * n
        for cost, end in graph[src]:
            pq.put((cost, 0, end))
        while not pq.empty():
            cost, transited, end = pq.get()
            if end == dst:
                return cost
            # 剩余中转次数，等于0代表这里就应当是终点了，当然并不是
            if transited == k:
                continue
            for item in graph[end]:
                cur_cost, cur_end = item
                next_cost = cur_cost + cost
                next_transited = transited + 1
                if next_cost < cost_to[cur_end]:
                    cost_to[cur_end] = next_cost
                    transited_to[cur_end] = next_transited
                # 通过最小值来防止死循环
                elif (
                    next_cost > cost_to[cur_end]
                    and next_transited > transited_to[cur_end]
                ):
                    continue
                pq.put((cur_cost + cost, next_transited, cur_end))
        return -1


# @lc code=end
