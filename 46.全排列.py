#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        long = len(nums)
        used = [False]*long
        path = []
        result = []

        def backtrack():
            if(len(path) == long):
                result.append(path.copy())
            for idx in range(long):
                if used[idx] == True:
                    continue
                used[idx] = True
                path.append(nums[idx])
                backtrack()
                path.pop()
                used[idx] = False
        backtrack()
        return result

# @lc code=end
