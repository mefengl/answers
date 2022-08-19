#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        long = len(candidates)
        val, res = [], []
        candidates = sorted(candidates)

        def bt(num, sumval):
            if sumval == target:
                res.append(val.copy())
                return
            if sumval > target:
                return
            for idx in range(num, long):
                if idx != num and candidates[idx] == candidates[idx - 1]:
                    continue
                val.append(candidates[idx])
                sumval += candidates[idx]
                bt(idx + 1, sumval)
                sumval -= candidates[idx]
                val.pop()

        bt(0, 0)
        return res


# @lc code=end
