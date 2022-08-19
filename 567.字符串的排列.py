#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = defaultdict(int), defaultdict(int)
        right, left = 0, 0
        valid = 0
        for s1_item in s1:
            need[s1_item] += 1
        lens2 = len(s2)
        lens1 = len(s1)
        lenneed = len(need)

        while right < lens2:
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 只要>=lens1都需要收缩
            # while right-left == lens1:
            # 这里的lens1和lenneed需要通过对算法的理解区分
            # 前者确认是排列，后者是valid
            while right - left >= lens1:
                if valid == lenneed:
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False


# @lc code=end
