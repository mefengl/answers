#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = defaultdict(int), defaultdict(int)
        for ti in t:
            need[ti] += 1
        left, right = 0, 0
        valid = 0
        long = len(s)
        needlong = len(need)
        start, length = 0, 2 * long
        while right < long:
            # 必要集
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1

            # 局部最优集
            while valid == needlong:
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        if length == 2 * long:
            return ""
        return s[start : start + length]
        # @lc code=end
