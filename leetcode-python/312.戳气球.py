#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        len_nums = len(nums)
        dp = [[0] * len_nums for _ in range(len_nums)]

        def last_coins(i: int, k: int, j: int) -> int:
            return nums[i] * nums[k] * nums[j]

        for i in reversed(range(len_nums)):
            # [i,j]表示一个区间，j当然需要大于等于i
            # 等于的情况便是默认的0
            for j in range(i + 1, len_nums):
                # 开区间(i,j)，这样k最后一个戳破的计算才合理，否则i,j已经被戳破这计算就不对了
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], last_coins(i, k, j) + dp[i][k] + dp[k][j])
        return dp[0][-1]


# @lc code=end
