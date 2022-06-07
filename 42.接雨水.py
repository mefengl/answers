#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    # 对于任意一个位置 i，能够装的水为左右两边最大的高度的较小值减去当前位置的高度
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax,rmax=[ height[0] ]+[0]*(n-1), [0]*(n-1)+[ height[-1] ]
        for i in range(1,n):
            lmax[i]=max(lmax[i-1],height[i])
        for i in range(n-2,-1,-1):
            rmax[i]=max(rmax[i+1],height[i])
        return sum(min(lmax[i],rmax[i])-height[i] for i in range(n))

# @lc code=end

