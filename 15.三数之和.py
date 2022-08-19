#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from unittest import result


def twoSum(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1
    res = []
    while l < r:
        lv, rv = nums[l], nums[r]
        sum = lv + rv
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            res.append([nums[l], nums[r]])
            while l < r and nums[l] == lv:
                l += 1
            while l < r and nums[r] == rv:
                r -= 1
    return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            zz = twoSum(nums[i + 1 :], -nums[i])
            for z in zz:
                res.append([nums[i]] + z)
        return res


# @lc code=end
