#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
import queue


def build_graph(heights: List[List[int]]) -> List[List[int]]:
    len_row = len(heights)
    len_col = len(heights[0])
    graph = [[] for _ in range(len_row * len_col)]
    directions = ((0, -1), (-1, 0), (1, 0), (0, 1))
    for row in range(len_row):
        for col in range(len_col):
            # 不能省略，二维数组的上下左右不是转置的
            # if row < col:
            #     continue
            cur_id = row * len_col + col
            for delta_row, delta_col in directions:
                next_row = row + delta_row
                next_col = col + delta_col
                # 防止越界
                if -1 < next_row < len_row and -1 < next_col < len_col:
                    next_id = next_row * len_col + next_col
                    cost = abs(heights[row][col] - heights[next_row][next_col])
                    graph[cur_id].append([cost, cur_id, next_id])
    return graph


def dijkstra(start: int, graph: List[List[int]]) -> List[int]:
    cost_to = [float("inf")] * len(graph)
    pq = queue.PriorityQueue()
    cost_to[start] = 0
    pq.put([0, start])
    while not pq.empty():
        cur_cost, start = pq.get()
        if cur_cost > cost_to[start]:
            continue
        for cost, _, next in graph[start]:
            cost_to_next = max(cur_cost, cost)
            if cost_to_next >= cost_to[next]:
                continue
            cost_to[next] = cost_to_next
            pq.put([cost_to_next, next])
    return cost_to


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        graph = build_graph(heights)
        cost_to = dijkstra(0, graph)
        len_row = len(heights)
        len_col = len(heights[0])
        return cost_to[len_row * len_col - 1]


# @lc code=end
