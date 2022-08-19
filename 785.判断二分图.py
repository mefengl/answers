#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start

# BFS
class Solution:
    def __init__(self):
        self.visited = []
        self.color = []
        self.bipartite = True

    def bfs(self, graph: List[List[int]], start: int):
        self.visited[start] = True
        q = collections.deque([start])
        while q:
            cur = q.popleft()
            for next in graph[cur]:
                if not self.visited[next]:
                    self.color[next] = not self.color[cur]
                    self.visited[next] = True
                    # 队列的新鲜血液不能丢
                    q.appendleft(next)
                elif self.visited[next]:
                    if self.color[next] == self.color[cur]:
                        self.bipartite = False
                        return

    def isBipartite(self, graph: List[List[int]]) -> bool:
        lengraph = len(graph)
        self.visited = [False] * lengraph
        self.color = [False] * lengraph
        for start in range(lengraph):
            if not self.visited[start]:
                self.bfs(graph, start)
        return self.bipartite


# # DFS
# class Solution:
#     def __init__(self):
#         self.bipartite = True
#         self.visited = []
#         self.color = []

#     def traverse(self, graph: List[List[int]], s: int):
#         if not self.bipartite:
#             return
#         self.visited[s] = True
#         for next in graph[s]:
#             # 没访问过就上反色
#             if not self.visited[next]:
#                 self.color[next] = not self.color[s]
#                 self.traverse(graph, next)
#             # 访问过就检查是否是反色
#             elif self.visited[next]:
#                 if self.color[next] == self.color[s]:
#                     self.bipartite = False
#                     return

#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         lengraph = len(graph)
#         self.visited = [False] * lengraph
#         self.color = [False] * lengraph
#         # 所有节点不一定相连，遍历所有子图
#         for idx in range(lengraph):
#             self.traverse(graph, idx)
#         return self.bipartite


# @lc code=end
