#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dp = [1 for _ in range(len_nums)]
        for i, _ in enumerate(dp):
            for j in range(i):
                # 严格递增，所以等于也不可
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


# @lc code=end
