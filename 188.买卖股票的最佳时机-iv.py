#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit_k_inf(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        if k > n // 2:
            return self.maxProfit_k_inf(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for _k in range(1, k + 1):
            dp[0][_k][1] = -prices[0]
        for i in range(1, n):
            for _k in range(1, k + 1):
                dp[i][_k][0] = max(dp[i - 1][_k][0], dp[i - 1][_k][1] + prices[i])
                dp[i][_k][1] = max(dp[i - 1][_k][1], dp[i - 1][_k - 1][0] - prices[i])
        return dp[-1][-1][0]


# @lc code=end
