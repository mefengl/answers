#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
def back_track(nums, used, path, res):
    if len(path) == len(nums):
        res.append(path.copy())
    for i, num in enumerate(nums):
        # not used[i-1] 用于至少用一次，否则到不了迭代终止处
        if i != 0 and not used[i - 1] and nums[i] == nums[i - 1]:
            continue
        if used[i]:
            continue
        path.append(num)
        used[i] = True
        back_track(nums, used, path, res)
        used[i] = False
        path.pop()


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 剪枝必备
        nums.sort()
        back_track(nums, [False] * len(nums), [], res)
        return res


# @lc code=end
