#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        M = 300
        dp = [[0] * (k + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, k + 1):
                # 鸡蛋碎或不碎
                dp[i][j] = 1 + dp[i - 1][j] + dp[i - 1][j - 1]
                # 这里的含义是覆盖所有层
                if dp[i][j] >= n:
                    return i


# @lc code=end
