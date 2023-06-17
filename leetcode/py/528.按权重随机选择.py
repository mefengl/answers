#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
from random import randint


class Solution:
    def __init__(self, w: List[int]):
        presum = [0] + w
        for idx in range(len(presum)):
            if idx == 0:
                presum[0]
                continue
            presum[idx] = presum[idx] + presum[idx - 1]
        self.presum = presum

    def pickIndex(self) -> int:
        presum = self.presum
        pick = randint(1, presum[-1])

        def right_bisect():
            lenpresum = len(presum)
            l, r = 0, lenpresum - 1
            while l <= r:
                m = l + (r - l) // 2
                if presum[m] > pick:
                    r = m - 1
                elif presum[m] < pick:
                    l = m + 1
                else:
                    r = m - 1
            return l

        pickidx = right_bisect() - 1
        return pickidx

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()
        # @lc code=end
