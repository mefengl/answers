#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from functools import reduce


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        len0 = len(nums)
        dis = 100000
        for x in range(len0):
            for y in range(x + 1, len0):
                for z in range(y + 1, len0):
                    asum = nums[x] + nums[y] + nums[z]
                    if abs(asum - target) < dis:
                        dis = abs(asum - target)
                        min = asum
        return min


# @lc code=end
