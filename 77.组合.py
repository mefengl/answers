#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start

# 二叉树遍历
def backtrack(nums: List[int], i: int, k: int, path: List[int], res: List[List[int]]):
    if len(path) == k:
        res.append(path)
        return
    if i == len(nums):
        return
    backtrack(nums, i + 1, k, path + [nums[i]], res)
    backtrack(nums, i + 1, k, path[:], res)


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        backtrack(list(range(1, n + 1)), 0, k, [], res)
        return res


# # 数学特性
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = [[]]
#         for num in range(1, n + 1):
#             res += [x + [num] for x in res]
#         return [x for x in res if len(x) == k]


# @lc code=end
