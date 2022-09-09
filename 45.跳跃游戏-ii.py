#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_jumps = [0] * len(nums)
        for i, num in enumerate(nums):
            max_jumps[i] = i + num
        res = 0
        lo = hi = 0
        # hi只需要达到数组最后一个序号即可，所以是len(nums)-1
        while hi < len(nums) - 1:
            lo, hi = hi, max(max_jumps[lo : hi + 1])
            res += 1
        return res


# @lc code=end
