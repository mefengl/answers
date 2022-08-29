#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start

# O(n*log(n))解法，耐心排序，二分搜索


def left_bi_search(nums: List[int], target: int) -> int:
    # 闭集合，len(nums)-1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            right = mid - 1
    # 边界有两种情况，0的话代表比top都小，放最左边
    # 越界的话，代表比top都大，新建pile
    return left


def poker_piles_num(nums: List[int]) -> int:
    len_nums = len(nums)
    top = []
    for idx, poker in enumerate(nums):
        put_idx = left_bi_search(top, poker)
        if put_idx == len(top):
            top.append(poker)
            continue
        top[put_idx] = poker
    return len(top)


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        heights = [x[1] for x in envelopes]
        len_heights = len(heights)
        return poker_piles_num(heights)


# # O(n^2)解法
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         envelopes.sort(key=lambda x: [x[0], -x[1]])
#         len_envelopes = len(envelopes)
#         dp = [1 for _ in range(len_envelopes)]
#         for i, _ in enumerate(dp):
#             for j in range(i):
#                 # 因为宽度严格递增的情况下，宽度上一定足够
#                 # 而且高度严格递减，统计高度的递增数列，也就是说相同宽度没有递增，所以相同宽度不会统计
#                 if envelopes[j][1] >= envelopes[i][1]:
#                     continue
#                 dp[i] = max(dp[j] + 1, dp[i])
#         return max(dp)


# @lc code=end
