#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        long = len(nums)
        val = []
        result = []
        nums = sorted(nums)

        def bt(num):
            result.append(val.copy())
            for idx in range(num, long):
                # idx越不越界和0没关系，和当前层数的最左有关
                # if idx != 0 and nums[idx] == nums[idx-1]:
                if idx != num and nums[idx] == nums[idx-1]:
                    continue
                val.append(nums[idx])
                bt(idx+1)
                val.pop()
        bt(0)
        return result
# @lc code=end
