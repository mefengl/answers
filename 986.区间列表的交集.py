#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]
            # 如果不是没有交集
            if not (a1 > b2 or a2 < b1):
                c1 = max(a1, b1)
                c2 = min(a2, b2)
                res.append([c1, c2])
            # 因为交集在右侧，所以是a2b2，因为b2已经在更右了，移动j绝无可能再产生交集
            if a2 <= b2:
                i += 1
            else:
                j += 1
        return res


# @lc code=end
