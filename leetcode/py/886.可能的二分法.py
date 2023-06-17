#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
class Solution:
    def __init__(self):
        self.visited = []
        self.color = []
        self.bipartition = True

    def buildGraph(self, n: int, dislikes: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for p1, p2 in dislikes:
            p1 -= 1
            p2 -= 1
            # 互相不喜欢
            graph[p1].append(p2)
            graph[p2].append(p1)
        return graph

    def traverse(self, graph: List[List[int]], start: int):
        if self.visited[start] or not self.bipartition:
            return
        self.visited[start] = True
        for next in graph[start]:
            if not self.visited[next]:
                self.color[next] = not self.color[start]
                self.traverse(graph, next)
            elif self.visited[next]:
                if self.color[next] == self.color[start]:
                    self.bipartition = False
                    return

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.visited = [False] * n
        self.color = [False] * n
        graph = self.buildGraph(n, dislikes)
        for idx in range(n):
            # 没有遍历过的子树才遍历，但是traverse函数开头已经把这一步实现了
            # if not self.visited[idx]:
            self.traverse(graph, idx)
        return self.bipartition


# @lc code=end
