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


# @lc code=end
