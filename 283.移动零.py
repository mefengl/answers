#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lennums = len(nums)
        f = s = 0
        while f < lennums:
            if nums[f] == 0:
                f += 1
                continue
            # 常规赋值
            nums[s] = nums[f]
            f += 1
            s += 1
        for idx in range(s, lennums):
            nums[idx] = 0


# @lc code=end
