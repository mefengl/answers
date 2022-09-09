#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start

# KMP
"""
ababc的状态转化表

+---+---+---+---+---+--+---+
|   | A | B | C | ? |  | X |
+---+---+---+---+---+--+---+
| 0 | 1 | 0 | 0 | 0 |  | 0 |
+---+---+---+---+---+--+---+
| 1 | 0 | 2 | 0 | 0 |  | 0 |
+---+---+---+---+---+--+---+
| 2 | 3 | 0 | 0 | 0 |  | 1 |
+---+---+---+---+---+--+---+
| 3 | 0 | 4 | 0 | 0 |  | 2 |
+---+---+---+---+---+--+---+
| 4 | 3 | 0 | 5 | 0 |  |   |
+---+---+---+---+---+--+---+

若char==chr(row)，则dp[row][char]=row+1
否则，dp[row][char]=dp[X][char]

X在row遍历完后更新，X=dp[X][row]，X之链连接起最长同前缀
"""


def build_dp(patten: str) -> List[List[int]]:
    n = len(patten)
    dp = [[0] * 256 for _ in range(n)]
    dp[0][ord(patten[0])] = 1
    x = 0
    for i in range(1, n):
        for j in range(256):
            dp[i][j] = dp[x][j]
        dp[i][ord(patten[i])] = i + 1
        x = dp[x][ord(patten[i])]
    return dp


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        dp = build_dp(needle)
        state = 0
        for i, char in enumerate(haystack):
            state = dp[state][ord(char)]
            if state == len(needle):
                # 这里的i是匹配字符串的末尾，返回开头，需要补1，就像abc匹配了，应该(-3+1)而不是(-3)
                return i - len(needle) + 1
        return -1


# # Rabin-Karp 算法
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         Q = 1658598167
#         L, R = len(needle), 256
#         # 最高位每单位
#         RL = R ** (L - 1)
#         target_hash = 0
#         for char in needle:
#             target_hash = ((R * target_hash) % Q + ord(char)) % Q left = right = 0
#         window_hash = 0
#         while right < len(haystack):
#             # 窗口右移
#             window_hash = ((R * window_hash) % Q + ord(haystack[right])) % Q
#             right += 1
#             if right - left == L:
#                 if window_hash == target_hash:
#                     if haystack[left:right] == needle:
#                         return left
#                 window_hash = (window_hash - RL * ord(haystack[left]) + Q) % Q
#                 left += 1
#         return -1


# if __name__ == "__main__":
#     S = Solution()
#     S.strStr("leetcode", "leeto")

# @lc code=end
