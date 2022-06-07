#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        self.memos = [-666]*(n+1)

        def dp(nn):
            memos = self.memos
            if nn == 0:
                return 0
            if nn == 1:
                return 1
            if memos[nn] != -666:
                return memos[nn]
            return dp(nn-1) + dp(nn-2)
        return dp(n)
# @lc code=end
