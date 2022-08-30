#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_dp = len(s)
        dp = [[0] * len_dp for _ in range(len_dp)]
        for idx in range(len_dp):
            dp[idx][idx] = 1
        for i in reversed(range(len_dp - 1)):
            for j in range(i + 1, len_dp):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]


# @lc code=end
