#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def __init__(self):
        self.visited = []
        self.onPath = []
        self.hasCycle = False

    def buildGraph(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[List[int]]:
        graph = [[] for _ in range(numCourses)]
        for dst, beg in prerequisites:
            graph[beg].append(dst)
        return graph

    def traverse(self, graph: List[List[int]], s: int):
        if self.onPath[s]:
            self.hasCycle = True
        if self.visited[s] or self.hasCycle:
            return
        self.visited[s] = True
        self.onPath[s] = True
        for item in graph[s]:
            self.traverse(graph, item)
        self.onPath[s] = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses
        graph = self.buildGraph(numCourses, prerequisites)
        # 并不是所有节点都相连
        for idx in range(numCourses):
            self.traverse(graph, idx)
        return not self.hasCycle


# @lc code=end
