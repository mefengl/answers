#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start


# 预处理法
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max, r_max = [0] * n, [0] * n
        l_max[0], r_max[-1] = height[0], height[-1]
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])
        for i in reversed(range(n - 1)):
            r_max[i] = max(r_max[i + 1], height[i])
        res = 0
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        return res


# # 双指针
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l, r = 0, len(height) - 1
#         l_max, r_max = 0, 0
#         res = 0
#         # < 或 <= 均可，因为l_max和r_max一定会有一个是all_max，l和r只会朝着all_max移动，而当区间重合时，那个点的高度是all_max，而此时l_max=r_max=all_max，所以体积为0
#         while l <= r:
#             l_max, r_max = max(l_max, height[l]), max(r_max, height[r])
#             # 体积由短板决定
#             if l_max < r_max:
#                 # 即使是短板，也是左边最长的短板
#                 res += l_max - height[l]
#                 # 已经计算过
#                 l += 1
#             else:
#                 res += r_max - height[r]
#                 r -= 1
#         return res


# @lc code=end
