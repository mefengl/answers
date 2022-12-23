#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for idx, _ in enumerate(dp):
            for coin in coins:
                if idx - coin < 0:
                    continue
                # 不能使用item，因为内循环中item是不变的
                # dp[idx] = min(dp[idx-coin]+1,item)
                dp[idx] = min(dp[idx - coin] + 1, dp[idx])
        res = dp[-1]
        if res == amount + 1:
            return -1
        return res


# @lc code=end
