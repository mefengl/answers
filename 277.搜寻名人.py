#
# @lc app=leetcode.cn id=277 lang=python3
#
# [277] 搜寻名人
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for other in range(n):
            # 如果candidate认识other或者other不认识candidate，candidate都不可能是名人
            if knows(candidate, other) or not knows(other, candidate):
                candidate = other
        for other in range(n):
            if other == candidate:
                continue
            if knows(candidate, other) or not knows(other, candidate):
                return -1
        return candidate


# @lc code=end
