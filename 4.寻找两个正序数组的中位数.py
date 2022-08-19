#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 单数mid，双数mid-1和mid（用[1]和[1,2]想单数和双数的情况）
        sumlen = len(nums1) + len(nums2)
        midlen = sumlen // 2
        flag1, flag2 = 0, 0
        newarr = []
        while len(newarr) < midlen + 1:
            if flag1 == len(nums1):
                newarr += nums2[flag2:]
                break
            if flag2 == len(nums2):
                newarr += nums1[flag1:]
                break
            if nums1[flag1] < nums2[flag2]:
                newarr.append(nums1[flag1])
                flag1 += 1
            else:
                newarr.append(nums2[flag2])
                flag2 += 1

        if sumlen % 2 == 0:
            return (newarr[midlen - 1] + newarr[midlen]) / 2
        return newarr[midlen]


# @lc code=end
