#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        numslen = len(nums)
        memos = [1] * len(nums)
        for index in range(numslen):
            for subindex in range(index):
                if nums[index] > nums[subindex]:
                    memos[index] = max(memos[index], memos[subindex] + 1)
        return max(memos)


# @lc code=end
