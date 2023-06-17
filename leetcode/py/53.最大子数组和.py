#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start

# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = nums.copy()
        for idx, _ in enumerate(nums):
            if idx == 0:
                continue
            # dp[idx] = max(dp[idx] + dp[idx - 1], dp[idx])
            nums[idx] = max(nums[idx] + nums[idx - 1], nums[idx])
        # return max(dp)
        return max(nums)


# # 前缀和
# def build_pre_sum(nums: List[int]) -> int:
#     presum = [0] + nums.copy()
#     for idx, _ in enumerate(presum):
#         if idx == 0:
#             continue
#         presum[idx] += presum[idx - 1]
#     return presum


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         presum = build_pre_sum(nums)
#         min_sum = presum[0]
#         for idx, sum_ in enumerate(presum):
#             if idx == 0:
#                 continue
#             max_sum = max(max_sum, sum_ - min_sum)
#             # 只能在后序更新，否则会出现自减
#             if sum_ < min_sum:
#                 min_sum = sum_
#         return max_sum


# @lc code=end
