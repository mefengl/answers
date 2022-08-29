#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(rem):
            memos = self.memos
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            if memos[rem] != -666:
                return memos[rem]

            mini = int(1e9)
            for coin in coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            self.memos[rem] = mini if mini < int(1e9) else -1
            return self.memos[rem]

        self.memos = [-666] * (amount + 1)
        return dp(amount)


# @lc code=end
