#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
def back_track(nums, start, target, path, res):
    sum_path = sum(path)
    if sum_path == target:
        res.append(path.copy())
        return
    for i in range(start, len(nums)):
        if i != start and nums[i] == nums[i - 1]:
            continue
        # nums从小到大，没必要遍历后面了
        if sum_path + nums[i] > target:
            break
        path.append(nums[i])
        back_track(nums, i + 1, target, path, res)
        path.pop()


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        back_track(candidates, 0, target, [], res)
        return res


# @lc code=end
