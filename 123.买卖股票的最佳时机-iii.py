#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_k = 2
        # dp[n][k][2]
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        dp[0][1][1] = -prices[0]
        dp[0][2][1] = -prices[0]
        for i in range(1, n):
            for k in range(1, max_k + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                # k only change when you buy
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][-1][0]


# @lc code=end
