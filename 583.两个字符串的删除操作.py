#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start


def longest_common_subsequence_num(word1: str, word2: str) -> int:
    len_row = len(word1) + 1
    len_col = len(word2) + 1
    dp = [[0] * len_col for _ in range(len_row)]
    for i in range(len_row):
        if i == 0:
            continue
        w1_idx = i - 1
        for j in range(len_col):
            if j == 0:
                continue
            w2_idx = j - 1
            if word1[w1_idx] == word2[w2_idx]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        lcs_num = longest_common_subsequence_num(word1, word2)
        return len_word1 + len_word2 - 2 * lcs_num


# @lc code=end
