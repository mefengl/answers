#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start

# 回溯法
def back_track(nums, used, path, res):
    if len(path) == len(nums):
        res.append(path.copy())
    for i, num in enumerate(nums):
        if used[i]:
            continue
        path.append(num)
        used[i] = True
        back_track(nums, used, path, res)
        used[i] = False
        path.pop()


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        back_track(nums, [False] * len(nums), [], res)
        return res


# # 切片语法
# def dfs(nums, path, res):
#     if len(nums) == 0:
#         res.append(path)
#         return
#     for i, num in enumerate(nums):
#         dfs(nums[:i] + nums[i + 1 :], path + [num], res)


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         dfs(nums, [], res)
#         return res


# @lc code=end
