#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#

# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 左下xy，右上ab
        area = 0
        corner_points = set()
        for x, y, a, b in rectangles:
            area += (a - x) * (b - y)
            for point in [(x, b), (a, b), (x, y), (a, y)]:
                # 只有奇数次才会留下来
                if point in corner_points:
                    corner_points.remove(point)
                else:
                    corner_points.add(point)
        # 奇数次应该只有四个角
        if len(corner_points) != 4:
            return False
        corner_points = sorted(list(corner_points))
        l_down, r_up = corner_points[0], corner_points[-1]
        return area == (r_up[0] - l_down[0]) * (r_up[1] - l_down[1])


# @lc code=end
