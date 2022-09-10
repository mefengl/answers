#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        cur_end = 0
        for _, end in intervals:
            if end > cur_end:
                res += 1
                cur_end = end
        return res


# @lc code=end
