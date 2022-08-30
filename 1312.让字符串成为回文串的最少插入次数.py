#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
def longest_palindrome_subsequence_value(s: str) -> int:
    len_s = len(s)
    dp = [[0] * len_s for _ in range(len_s)]
    for i in range(len_s):
        dp[i][i] = 1
    for i in reversed(range(len_s - 1)):  # [len_s-2...0]
        for j in range(i + 1, len_s):  # [i+1...len_s-1]
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    return dp[0][-1]


class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s) - longest_palindrome_subsequence_value(s)


# @lc code=end
