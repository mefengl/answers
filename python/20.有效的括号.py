#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    left_of = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s: str) -> bool:
        left = []
        for c in s:
            if c in ["(", "[", "{"]:
                left.append(c)
            elif left and left[-1] == self.left_of[c]:
                left.pop()
            else:
                return False
        if left:
            return False
        return True


# @lc code=end
