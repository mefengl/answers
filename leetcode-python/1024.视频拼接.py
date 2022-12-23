#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#

# @lc code=start

# 跳跃游戏
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        max_jumps = [0] * 101  # end<=100
        for start, end in clips:
            max_jumps[start] = max(max_jumps[start], end)

        res = 0
        lo = hi = 0
        while hi < time:
            lo, hi = hi, max(max_jumps[lo : hi + 1])
            # 等于也不行，因为意味着不能再往前一步了
            if lo >= hi:
                return -1
            res += 1
        return res


# # labuladong
# class Solution:
#     def videoStitching(self, clips: List[List[int]], time: int) -> int:
#         n = len(clips)
#         # 起点升序，终点降序
#         clips.sort(key=lambda x: (x[0], -x[1]))
#         count = 0
#         i = 0
#         cur_end = next_end = 0
#         while i < n:
#             if clips[i][0] > cur_end:
#                 return -1
#             # 这个判断有点多余，因为next_end的过程可以覆盖这一步
#             # if clips[i][1] <= cur_end:
#             #     i+=1
#             #     continue
#             while i < n and clips[i][0] <= cur_end:
#                 next_end = max(next_end, clips[i][1])
#                 i += 1
#             count += 1
#             cur_end = next_end
#             if cur_end >= time:
#                 return count
#         return -1


# @lc code=end
