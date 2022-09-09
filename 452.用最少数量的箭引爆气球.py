#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[1])
        early_end = points[0][1]
        # 最早结束的气球边界一定选中，所以初始为1
        res = 1
        for i in range(1, n):
            # > 而不是 >=，是因为边界重合的气球同样一箭引爆，只能加1
            if points[i][0] > early_end:
                res += 1
                early_end = points[i][1]
        return res


# @lc code=end
