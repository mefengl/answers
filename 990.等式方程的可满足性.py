#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
NUMBER_OF_LETTERS = 26
ORD_OF_SMALL_A = ord("a")


class UnionFind:
    def __init__(self, count: int):
        self.__count = count
        self.__parent = [i for i in range(count)]

    def __find(self, node):
        if self.__parent[node] != node:
            # 这一步使得return find没有必要，因为高效的find总是要修改的
            self.__parent[node] = self.__find(self.__parent[node])
        return self.__parent[node]

    def is_connected(self, node1, node2):
        root1 = self.__find(node1)
        root2 = self.__find(node2)
        return root1 == root2

    def union(self, node1, node2):
        root1 = self.__find(node1)
        root2 = self.__find(node2)
        if root1 == root2:
            return
        # 要相同根节点，只能让根节点「贼父做父」
        self.__parent[root2] = root1


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(NUMBER_OF_LETTERS)
        for x, *eql, y in equations:
            if eql[0] == "=":
                x_idx = ord(x) - ORD_OF_SMALL_A
                y_idx = ord(y) - ORD_OF_SMALL_A
                uf.union(x_idx, y_idx)
        for x, *eql, y in equations:
            if eql[0] == "!":
                x_idx = ord(x) - ORD_OF_SMALL_A
                y_idx = ord(y) - ORD_OF_SMALL_A
                if uf.is_connected(x_idx, y_idx):
                    return False
        return True


# @lc code=end
