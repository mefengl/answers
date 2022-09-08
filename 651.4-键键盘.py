#
# @lc app=leetcode.cn id=651 lang=python3
#
# [651] 4键键盘
#

# @lc code=start
class Solution:
    def maxA(self, n: int) -> int:
        # 实际只有三键，A键，全选复制键，和粘贴键
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            # j表示全选复制结束时的索引
            # 至少比2大，这样能完成全选复制，比i小，至少有一次的粘贴机会
            for j in range(2, i):
                # dp[i]可以代表dp[j-2]和2次机会用来按全选复制键和(i-j-1)次的机会用来按粘贴键
                # i-j是粘贴键使用的次数，翻的倍数是次数加1，比如：粘贴1次，是原来的2倍；粘贴2次，是原来的3倍
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[-1]


# @lc code=end
