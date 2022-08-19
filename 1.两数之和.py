# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        nums = [[x, y] for x, y in enumerate(nums)]
        nums.sort(key=lambda x: x[1])
        while l < r:
            lv, rv = nums[l][1], nums[r][1]
            sum = lv + rv
            if sum < target:
                while l < r and nums[l][1] == lv:
                    l += 1
            elif sum > target:
                while l < r and nums[r][1] == rv:
                    r -= 1
            else:
                return [nums[l][0], nums[r][0]]


# @lc code=end
