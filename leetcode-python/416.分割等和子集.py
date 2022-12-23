#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 选前n个元素，能否装满sum/2的背包
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        weight = sum_nums // 2
        len_row = len(nums) + 1
        len_col = weight + 1
        dp = [[False] * len_col for _ in range(len_row)]
        # weight为0，即空集，已经装满
        for i, _ in enumerate(dp):
            dp[i][0] = True

        for i, _ in enumerate(dp):
            # 没有选，肯定装不满
            if i == 0:
                continue
            idx_num = i - 1
            for j, _ in enumerate(dp[0]):
                if j == 0:
                    continue
                # 当前物体装不了，只能不装，和前n-1里选择是一样的
                if nums[idx_num] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 装或不装
                    dp[i][j] = dp[i - 1][j - nums[idx_num]] or dp[i - 1][j]
        return dp[-1][-1]


# @lc code=end
