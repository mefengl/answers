#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            start, end = interval
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(interval)
        return res


# @lc code=end
