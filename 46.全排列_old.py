#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
def dfs(nums: List[int], path: List[int], res: List[List[int]]) -> None:
    if len(nums) == 0:
        res.append(path)
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], res)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        dfs(nums, [], res)
        return res


# # 回溯法
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         long = len(nums)
#         used = [False] * long
#         path = []
#         result = []

#         def backtrack():
#             if len(path) == long:
#                 result.append(path.copy())
#             for idx in range(long):
#                 if used[idx] == True:
#                     continue
#                 used[idx] = True
#                 path.append(nums[idx])
#                 backtrack()
#                 path.pop()
#                 used[idx] = False

#         backtrack()
#         return result

# @lc code=end
