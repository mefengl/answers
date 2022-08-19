#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), 500 * 5 * 10000

        def f(x):
            x0 = x
            currentdays = 0
            lenweights = len(weights)
            for idx in range(lenweights):
                if x0 < weights[idx]:
                    currentdays += 1
                    x0 = x
                x0 -= weights[idx]
            return x

        while left < right:
            mid = left + (right - left) // 2
            if f(mid) < days:
                right = mid - 1
            elif f(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
        return left


# @lc code=end
