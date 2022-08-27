#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums += list(range(len(nums) + 1))
        res = 0
        for num in nums:
            res ^= num
        return res


# @lc code=end
