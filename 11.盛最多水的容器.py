# @before-stub-for-debug-begin
from python3problem11 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        area = 0
        while l<r:
            hl,hr = height[l],height[r]
            ans = min(hl,hr)*(r-l)
            area = max(area,ans)
            if hl>hr:
                r -= 1
            else:
                l += 1
        return area




# @lc code=end

