#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
class Pair:
    def __init__(self):
        self.fir = 0
        self.sed = 0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        # [先手，后手]
        dp = [[Pair() for _ in range(len_nums)] for _ in range(len_nums)]
        # 初始化
        for i, num in enumerate(nums):
            # i==j时，先手获得一切
            dp[i][i].fir = num
        for i in reversed(range(len_nums)):
            for j in range(i + 1, len_nums):
                left = nums[i] + dp[i + 1][j].sed
                right = nums[j] + dp[i][j - 1].sed
                # 一回合，先手和后手，或者说是先手和少一堆的先手
                if left >= right:
                    dp[i][j].fir = left
                    # 后手是i被拿了之后的先手
                    dp[i][j].sed = dp[i + 1][j].fir
                else:
                    dp[i][j].fir = right
                    # 后手是j被拿了之后的先手
                    dp[i][j].sed = dp[i][j - 1].fir
        return dp[0][-1].fir >= dp[0][-1].sed


# @lc code=end
