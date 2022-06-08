#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = f = 0
        lennums = len(nums)
        while f < lennums:
            if nums[f] == val:
                f += 1
                continue
            nums[s] = nums[f]
            s += 1
            f += 1
        return s


# @lc code=end


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         slow,fast=0,0
#         while fast<len(nums):
#             if nums[fast]!=val:
#                 nums[slow]=nums[fast]
#                 slow+=1
#             fast+=1
#         return slow
