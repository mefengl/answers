#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = j = 0
        for c in t:
            if c == s[i]:
                if i == len(s) - 1:
                    return True
                i += 1
        return False


# @lc code=end
