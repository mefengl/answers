#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        early_end = intervals[0][1]
        res = 0
        for i in range(1, n):
            if intervals[i][0] < early_end:
                # 需要去除
                res += 1
            else:
                # start大于等于当前early_end的最早的end，就是下一个early_end
                early_end = intervals[i][1]
        return res


# @lc code=end
