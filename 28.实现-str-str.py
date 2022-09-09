#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
# Rabin-Karp 算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        Q = 1658598167
        L, R = len(needle), 256
        # 最高位每单位
        RL = R ** (L - 1)
        target_hash = 0
        for char in needle:
            target_hash = ((R * target_hash) % Q + ord(char)) % Q left = right = 0
        window_hash = 0
        while right < len(haystack):
            # 窗口右移
            window_hash = ((R * window_hash) % Q + ord(haystack[right])) % Q
            right += 1
            if right - left == L:
                if window_hash == target_hash:
                    if haystack[left:right] == needle:
                        return left
                window_hash = (window_hash - RL * ord(haystack[left]) + Q) % Q
                left += 1
        return -1


# if __name__ == "__main__":
#     S = Solution()
#     S.strStr("leetcode", "leeto")

# @lc code=end
