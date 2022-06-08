#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        val = []
        long = len(nums)

        def backtrack(num):
            result.append(val.copy())
            for idx in range(num, long):
                val.append(nums[idx])
                backtrack(idx+1)
                val.pop()
        backtrack(0)
        return result

# @lc code=end
