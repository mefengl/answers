#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
INIT_VALUE = 0


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_row = len(text1) + 1
        len_col = len(text2) + 1
        dp = [[INIT_VALUE] * len_col for _ in range(len_row)]
        for i in range(len_row):
            if i == 0:
                continue
            text1_index = i - 1
            for j in range(len_col):
                if j == 0:
                    continue
                text2_index = j - 1
                if text1[text1_index] != text2[text2_index]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if text1[text1_index] == text2[text2_index]:
                    # 取左上角，因为每个字母只能计算一次，如果取上和左的话，其实包含了text1或text2重复选取的风险
                    dp[i][j] = 1 + dp[i - 1][j - 1]
        return dp[-1][-1]


# @lc code=end
