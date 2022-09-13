#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start

# 组合有start因为顺序也很重要
def back_track(nums, start, target, path, res):
    sum_path = sum(path)
    if sum_path == target:
        res.append(path.copy())
    for i in range(start, len(nums)):
        if nums[i] + sum_path > target:
            return
        path.append(nums[i])
        # 从i而不是i+1开始，就可以重复选
        back_track(nums, i, target, path, res)
        path.pop()


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        back_track(candidates, 0, target, [], res)
        return res


# @lc code=end
