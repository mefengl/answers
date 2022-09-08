#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(2, len(nums) + 2):
            # dp[i+1]是不抢，nums[i]+dp[i+2]显然是抢
            dp[i] = max(dp[i - 1], nums[i - 2] + dp[i - 2])
        return dp[-1]


# @lc code=end
