#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums) - 1
        nmin = n
        while n > 0:
            n -= 1
            if nums[n] < nums[n + 1]:
                break
        while nmin > 0:
            if nums[nmin] > nums[n]:
                break
            nmin -= 1
        if nmin == 0:
            nums.sort()
            return
        nums[nmin], nums[n] = nums[n], nums[nmin]
        nums[n + 1 :] = sorted(nums[n + 1 :])
        """
        Do not return anything, modify nums in-place instead.
        """


# @lc code=end
