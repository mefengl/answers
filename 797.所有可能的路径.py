#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []

    def traverse(self, graph: List[List[int]], s: int, path: List[int]):
        path.append(s)
        n = len(graph)
        if s == n - 1:
            self.res.append(path.copy())
            path.pop()
            return
        for item in graph[s]:
            self.traverse(graph, item, path)
        path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.traverse(graph, 0, [])
        return self.res


# @lc code=end
