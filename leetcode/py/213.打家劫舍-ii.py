#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def _rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(2, len(nums) + 2):
            dp[i] = max(dp[i - 1], nums[i - 2] + dp[i - 2])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))


# @lc code=end
