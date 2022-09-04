#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        len_row = len(coins)+1
        len_col = amount+1
        dp = [[0]*len_col for _ in range(len_row)]
        for i,_ in enumerate(dp):
            # 所凑金额为0，则只能什么都不做
            dp[i][0] = 1
        
        for i,_ in enumerate(dp):
            if i==0:continue
            idx_coins = i -1 
            for j,_ in enumerate(dp[0]):
                if j==0:continue
                # 币值过大
                if j < coins[idx_coins]:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 3种硬币凑出5 = 2个硬币凑出5 + 3种硬币凑出(5-第三个币值) ，后者带来重复选
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[idx_coins]]
        return dp[-1][-1]
                

# @lc code=end
