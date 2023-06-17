#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lennums = len(nums)
        if lennums == 0:
            return 0
        fast, slow = 0, 0
        while fast < lennums:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        # 第一个不用slow赋值，返回时需考虑
        return slow + 1


# @lc code=end
