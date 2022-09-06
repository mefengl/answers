#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#

# @lc code=start
MAX_RES = 100 * 100 * 2


# # 自底向上动态规划
# class Solution:
#     def __init__(self):
#         self.char_to_index = collections.defaultdict(set)

#     def findRotateSteps(self, ring: str, key: str) -> int:
#         for i, item in enumerate(ring):
#             self.char_to_index[item].add(i)
#         # 注意：key为每行，ring为每列
#         len_row = len(key) + 1
#         len_col = len(ring)
#         dp = [[MAX_RES] * len_col for _ in range(len_row)]
#         # 第0行初始值应为ring归正的距离，因为第1行的是在ring归正的情况下展开的，如果初始化为0，第1行就等于是说ring处在任意当前字母
#         # dp[0] = [0]*len_col
#         dp[0] = [min(idx, len_col - idx) for idx, _ in enumerate(dp[0])]
#         for i, _ in enumerate(dp):
#             if i == 0:
#                 continue
#             key_char = key[i - 1]
#             for j, _ in enumerate(dp[0]):
#                 for k in self.char_to_index[key_char]:
#                     # dp[i-1][k]表示上一行，也就是上一个key到当前key最小距离（k为和当前key值相同的不同序号）
#                     # i除了表示在key中的索引外，和任何ring上的距离关系无关
#                     dp[i][j] = min(
#                         dp[i][j], dp[i - 1][k] + min(abs(j - k), len_col - abs(j - k))
#                     )
#         [print(x) for x in dp]
#         return min(dp[-1]) + len(key)


# 递归消除子问题
class Solution:
    def __init__(self):
        self.memo = {}
        self.char_to_index = collections.defaultdict(set)

    def dp(self, ring: str, i: int, key: str, j: int) -> int:
        if j == len(key):
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        res = MAX_RES
        for item in self.char_to_index[key[j]]:
            delta = abs(item - i)
            delta = min(delta, len(ring) - delta)
            sub_problem = self.dp(ring, item, key, j + 1)
            res = min(res, 1 + delta + sub_problem)
        self.memo[(i, j)] = res
        return res

    def findRotateSteps(self, ring: str, key: str) -> int:
        for i, char in enumerate(ring):
            self.char_to_index[char].add(i)
        return self.dp(ring, 0, key, 0)


# @lc code=end
