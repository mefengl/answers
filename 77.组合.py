#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        val = []

        def bt(num):
            # len(val)决定层数，而不是num(idx+1)，那只是选择
            if len(val) == k:
                result.append(val.copy())
                return
            for idx in range(num, n+1):
                val.append(idx)
                bt(idx+1)
                val.pop()
        bt(1)
        return result

# @lc code=end
