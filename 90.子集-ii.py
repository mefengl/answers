#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
from typing import List


# @lc code=start
def back_track(nums: List[int], start: int, path: List[int], res: List[List[int]]):
    res.append(path)
    for i in range(start, len(nums)):
        # 确保是同一层
        if i != start and nums[i] == nums[i - 1]:
            continue
        path.append(nums[i])
        back_track(nums, i + 1, path[:], res)
        path.pop()


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        back_track(nums, 0, [], res)
        return res


# if __name__ == "__main__":
#     Solution().subsetsWithDup([1,2,2])
# @lc code=end
