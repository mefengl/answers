#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start

# DFS
class Solution:
    def __init__(self):
        self.bipartite = True
        self.visited = []
        self.color = []

    def traverse(self, graph: List[List[int]], s: int):
        if not self.bipartite:
            return
        self.visited[s] = True
        for next in graph[s]:
            # 没访问过就上反色
            if not self.visited[next]:
                self.color[next] = not self.color[s]
                self.traverse(graph, next)
            # 访问过就检查是否是反色
            elif self.visited[next]:
                if self.color[next] == self.color[s]:
                    self.bipartite = False
                    return

    def isBipartite(self, graph: List[List[int]]) -> bool:
        lengraph = len(graph)
        self.visited = [False] * lengraph
        self.color = [False] * lengraph
        # 所有节点不一定相连，遍历所有子图
        for idx in range(lengraph):
            self.traverse(graph, idx)
        return self.bipartite


# @lc code=end
