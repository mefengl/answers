#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, R = 10, 4
        RL = R ** (L - 1)
        dna_to_num = {"A": 0, "G": 1, "C": 2, "T": 3}
        nums = [dna_to_num[dna] for dna in s]
        seen, res = set(), set()
        window_hash = 0
        left = right = 0
        while right < len(nums):
            window_hash = R * window_hash + nums[right]
            right += 1
            if right - left == L:
                if window_hash in seen:
                    res.add(s[left:right])
                else:
                    seen.add(window_hash)
                # 去除最高位
                window_hash -= nums[left] * RL
                left += 1
        return list(res)


# @lc code=end
