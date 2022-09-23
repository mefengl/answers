#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start


from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = defaultdict(int), defaultdict(int)
        # 这个错找了很久，起源便是need_item，应该是p_item
        # for need_item in need:
        for p_item in p:
            need[p_item] += 1
        right, left = 0, 0
        valid = 0
        lens, lenp = len(s), len(p)
        lenneed = len(need)
        res = []
        while right < lens:
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= lenp:
                if valid == lenneed:
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res


# @lc code=end
