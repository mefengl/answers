#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start


def _findntarget(nums: List[int], n: int, target: int) -> List[List[int]]:
    nums.sort()
    res = []
    if n == 2:
        l, r = 0, len(nums) - 1
        while l < r:
            lv, rv = nums[l], nums[r]
            sum = lv + rv
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                res.append([lv, rv])
                while l < r and nums[l] == lv:
                    l += 1
                while l < r and nums[r] == rv:
                    r -= 1
    else:
        return [
            [nums[i]] + z
            for i in range(len(nums) - n + 1)
            if not (i > 0 and nums[i] == nums[i - 1])
            for z in _findntarget(nums[i + 1 :], n - 1, target - nums[i])
        ]
    return res


def findntarget(nums: List[int], n: int, target: int) -> List[List[int]]:
    nums.sort()
    return _findntarget(nums, n, target)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return findntarget(nums, 4, target)


# @lc code=end
