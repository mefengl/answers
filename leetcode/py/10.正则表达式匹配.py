#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        len_row = len(s) + 1
        len_col = len(p) + 1
        dp = [[False] * len_col for _ in range(len_row)]
        dp[0][0] = True
        for i in range(len_row):
            for j in range(1, len_col):
                if p[j - 1] != "*":
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # *的匹配0次的情况
                    dp[i][j] |= dp[i][j - 2]
                    if match(i, j - 1):
                        # 舍去s片段末尾能匹配的一位
                        dp[i][j] |= dp[i - 1][j]
        [print(x) for x in dp]
        return dp[-1][-1]


# @lc code=end
