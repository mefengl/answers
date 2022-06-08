#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start


class Solution:
    def palindrome(self, s, l, r):
        lens = len(s)
        while l >= 0 and r < lens and s[l] == s[r]:
            l -= 1
            r += 1
        # 退出条件是s[l]!=s[r]，内移1位
        return s[l+1: r]

    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        res = ""
        lenres = len(res)
        for idx in range(lens):
            s1 = self.palindrome(s, idx, idx)
            s2 = self.palindrome(s, idx, idx+1)
            lens1, lens2 = len(s1), len(s2)
            if lens1 > lenres:
                res = s1
                lenres = lens1
            if lens2 > lenres:
                res = s2
                lenres = lens2
        return res

        # @lc code=end
