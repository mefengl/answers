#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] 会议室 II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        begins = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        res = 0
        count = 0
        # 时间线上，正序和逆序去遍历是一样的，这里正序遍历
        n = len(intervals)
        i = j = 0
        # 正序begins一定会先遍历完，即i==n，这时候count的最大值已经得到，没必要继续
        while i < n:
            if begins[i] < ends[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res


# @lc code=end
