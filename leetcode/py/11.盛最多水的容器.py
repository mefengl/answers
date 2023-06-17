#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

from typing import List

# @lc code=start

# 双指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max = r_max = 0
        res = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            res = max(res, min(l_max, r_max) * (r - l))
            # 移动短板边界
            if l_max < r_max:
                l += 1
            else:
                r -= 1
        return res


# # 预处理法，O(n^2)，超时
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         l_max, r_max = [0] * n, [0] * n
#         l_max[0],r_max[-1] = height[0],height[-1]
#         for i in range(1, n):
#             l_max[i] = max(l_max[i - 1], height[i])
#         for i in reversed(range(n - 1)):
#             r_max[i] = max(r_max[i + 1], height[i])
#         res = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 area = min(l_max[i], r_max[j]) * (j - i)
#                 res = max(res, area)
#         return res


# if __name__ == "__main__":
#     Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
# @lc code=end
