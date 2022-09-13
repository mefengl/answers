#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start

# # 二叉树遍历
# def dfs(nums,i,path,res):
#     if i == len(nums):
#         res.append(path)
#         return
#     dfs(nums, i+1, path+[nums[i]], res)
#     dfs(nums, i+1, path[:], res)

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         dfs(nums, 0,[], res)
#         return res

# 数学
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [x + [num] for x in res]
        return res


# @lc code=end
