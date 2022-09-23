#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
# 二维平面的最长子序列问题
# 宽度升序，保证一维包含
# 高度降序，保证二维不包含重复宽度（同样宽度下，高度前面的高度只可能比它大，所以不会重复）
#

# @lc code=start
import functools


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        se = sorted(
            envelopes,
            key=functools.cmp_to_key(
                lambda x, y: 1
                if x[0] > y[0]
                else -1
                if x[0] < y[0]
                else 1
                if x[1] < y[1]
                else -1
                if x[1] > y[1]
                else 0
            ),
        )

        def lengthofLIS(nums: List[int]):
            long = len(nums)
            top = [-666] * (long + 1)
            piles = 0
            for idx in range(long):
                poker = nums[idx]
                l, r = 0, piles
                while l <= r:
                    m = l + (r - l) // 2
                    if top[m] > poker:
                        r = m - 1
                    elif top[m] < poker:
                        l = m + 1
                    else:
                        r = m - 1
                if l > piles:
                    piles += 1
                top[l] = poker
            return piles

        height = [x[1] for x in se]
        return lengthofLIS(height)
        # @lc code=end
