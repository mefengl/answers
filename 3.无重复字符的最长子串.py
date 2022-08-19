#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        right, left = 0, 0
        maxres = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] >= 2:
                d = s[left]
                left += 1
                window[d] -= 1
            maxres = max(maxres, right - left)
        return maxres


# @lc code=end
