#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
"""
+-----------+-------+
| 替换/跳过 | 插入/ |
+-----------+-------+
| 删除/     | +1/+0 |
+-----------+-------+

+----+----+---+---+---+---+---+
|    | "" | h | o | r | s | e |
+----+----+---+---+---+---+---+
| "" | 0  | 1 | 2 | 3 | 4 | 5 |
+----+----+---+---+---+---+---+
| r  | 1  | 1 | 2 | 3 | 4 | 5 |
+----+----+---+---+---+---+---+
| o  | 2  | 2 | 1 | 2 | 3 | 4 |
+----+----+---+---+---+---+---+
| s  | 3  | 3 | 2 | 2 | 2 | 3 |
+----+----+---+---+---+---+---+

初始值：一个空串变成"",a,ap,app…分别需要0，1，2，3步
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 从上表也能看出，要加工的字符串word1是column，而且还要加入空串
        len_col = len(word1) + 1
        len_row = len(word2) + 1
        # 初始值：一个空串变成"",a,ap,app…分别需要0，1，2，3步
        dp = [[0] * len_col for _ in range(len_row)]
        dp[0] = list(range(len_col))
        for i in range(len_row):
            if i == 0:
                continue
            word2_idx = i - 1
            for j in range(len_col):
                if j == 0:
                    # 和dp[0]的初始值逻辑相同，空串的基础上插入字符串
                    dp[i][j] = dp[i - 1][j] + 1
                    continue
                word1_idx = j - 1
                if word1[word1_idx] == word2[word2_idx]:
                    # 不用+1操作
                    dp[i][j] = dp[i - 1][j - 1]
                    continue
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


# @lc code=end
