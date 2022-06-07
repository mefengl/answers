#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,mid,right = 0,len(nums)//2,len(nums)
        while True:
            if left >= right:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid
            mid = (right-left)//2 + left

# @lc code=end

