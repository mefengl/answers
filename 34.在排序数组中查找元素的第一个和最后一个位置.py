#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bisect(nums, target):
            l, r = 0, len(nums)-1
            while(l <= r):
                m = l + (r-l)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            if l >= len(nums) or nums[l] != target:
                return -1
            return l

        def right_bisect(nums, target):
            l, r = 0, len(nums)-1
            while(l <= r):
                m = l + (r-l)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    l = m + 1
            if r < 0 or nums[r] != target:
                return -1
            return r
        return([left_bisect(nums, target), right_bisect(nums, target)])

# @lc code=end
