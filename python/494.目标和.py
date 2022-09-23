#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start

# 动态规划
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        分到+号的，比分到-号的多target，
        由此，sum(+)-sum(-) = target，
        又，sum(+)+sum(1) = sum(nums)，
        左右相加，得 2 * sum(+) = target + sum(nums)，
        即，sum(+) = (target + sum(nums)) // 2
        """
        sum_nums = sum(nums)
        if abs(target) > sum_nums:
            return 0
        two_times_sum_plus = target + sum_nums
        if two_times_sum_plus % 2 != 0:
            return 0
        sum_plus = two_times_sum_plus // 2
        len_row = len(nums) + 1
        len_col = sum_plus + 1
        dp = [[0] * len_col for _ in range(len_row)]
        # 只存在这一种情况，无物可选凑出非0不存在
        dp[0][0] = 1
        for i, _ in enumerate(dp):
            dp[i][0] = 1
        for i, _ in enumerate(dp):
            if i == 0:
                continue
            for j, _ in enumerate(dp[0]):
                # j需要从0遍历，nums[i-1]为0的情况下，需要更新值的，因为+0-0都可以凑出0，遍历的话，刚好 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 0]达到了这一效果
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]


# # 回溯法：O(n^2)，回溯法一定不能忘记备忘录消除重复子问题
# class Solution:
#     def __init__(self):
#         self._memo = {}

#     def _backtrace(self, nums, i, remain):
#         if i == len(nums):
#             if remain == 0:
#                 return 1
#             return 0
#         if (i,remain) in self._memo:
#             return self._memo[(i,remain)]
#         res = self._backtrace(nums,i+1,remain+nums[i]) + self._backtrace(nums,i+1,remain-nums[i])
#         self._memo[(i,remain)] = res
#         return res

#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         return self._backtrace(nums, 0, target)


# @lc code=end
