#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.visited = []
        self.onPath = []
        self.res = []
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
        self.visited[s] = self.onPath[s] = True
        for item in graph[s]:
            self.traverse(graph, item)
        self.onPath[s] = False
        # 后序遍历没有重复的问题，树遍历没有重复的问题，一个节点不会遍历两遍，图加上visited数组后同样不会重复
        self.res.append(s)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses
        graph = self.buildGraph(numCourses, prerequisites)
        for idx in range(numCourses):
            self.traverse(graph, idx)
        # 这算法是beg->[dst]的类多叉树，后序遍历需要reverse
        return [] if self.hasCycle else list(reversed(self.res))


# @lc code=end
