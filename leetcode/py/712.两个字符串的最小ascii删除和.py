#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#

# @lc code=start
def ord_sum(s: str) -> int:
    return sum([ord(c) for c in s])


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len_row = len(s1) + 1
        len_col = len(s2) + 1
        s1_ord = [ord(c) for c in s1]
        s2_ord = [ord(c) for c in s2]
        # 初始化
        dp = [[0] * len_col for _ in range(len_row)]
        for i in range(len_row):
            if i == 0:
                continue
            s1_idx = i - 1
            for j in range(len_col):
                if j == 0:
                    continue
                s2_idx = j - 1
                if s1[s1_idx] == s2[s2_idx]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[s1_idx])
                else:
                    # 找出要被删除的ASCII值最大的公共子序列，不是最小
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return ord_sum(s1) + ord_sum(s2) - 2 * dp[-1][-1]


# @lc code=end
