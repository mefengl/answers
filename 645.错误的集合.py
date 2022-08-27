#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        for idx in range(0, len(nums)):
            match_idx = abs(nums[idx]) - 1
            if nums[match_idx] < 0:
                dup = match_idx
                continue
            nums[match_idx] *= -1
        mis = 0
        for idx, num in enumerate(nums):
            if num > 0:
                mis = idx
                break
        return [dup + 1, mis + 1]


# @lc code=end
