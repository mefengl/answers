#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        delta = [gas[i] - cost[i] for i in range(n)]
        # 整体不足
        if sum(delta) < 0:
            return -1
        # 最低点必够
        for i in range(1, n):
            delta[i] += delta[i - 1]
        return (delta.index(min(delta)) + 1) % n


# @lc code=end
