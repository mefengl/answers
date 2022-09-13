#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from typing import List

# @lc code=start


# 不明白的方法
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, m = divmod(sum(nums), k)
        if m != 0:
            return False
        dp = [0] * k
        n = len(nums)
        nums.sort(reverse=True)
        # 剪枝之最大元素没有桶可以装
        if nums[0] > target:
            return False

        def dfs(i: int):
            if i == n:
                # 数字相等
                return len(set(dp)) == 1
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target and dfs(i + 1):
                    return True
                dp[j] -= nums[i]
                # 后面空桶是等价的，如果这个空桶，装下nums[i]不可能，那么后面所有空桶装下它都不可能
                if dp[j] == 0:
                    break
            return False

        return dfs(0)


# if __name__ == "__main__":
#     Solution().canPartitionKSubsets(
#         [3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10
#     )

# @lc code=end
