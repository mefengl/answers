#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def __init__(self):
        self.memo = []

    def count(self, lo: int, hi: int) -> int:
        if lo > hi:
            return 1
        if (memo := self.memo[lo][hi]) != 0:
            return memo
        res = 0
        for mid in range(lo, hi + 1):
            left = self.count(lo, mid - 1)
            right = self.count(mid + 1, hi)
            # 组合问题是乘积关系
            res += left * right
        self.memo[lo][hi] = res
        return res

    def numTrees(self, n: int) -> int:
        self.memo = [[0] * (n + 1) for _ in range(n + 1)]
        return self.count(1, n)


# @lc code=end
