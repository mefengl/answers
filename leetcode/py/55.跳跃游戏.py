#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, num in enumerate(nums):
            # 已经无法到达i了
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + num)
        return True


# @lc code=end
