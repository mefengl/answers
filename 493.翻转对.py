#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Merge:
    def __init__(self):
        self.temp = []
        self.count = 0

    def sort(self, nums):
        lennums = len(nums)
        self.temp = [0] * lennums
        self._sort(nums, 0, lennums - 1)

    def _sort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self._sort(nums, lo, mid)
        self._sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        for idx in range(lo, hi + 1):
            self.temp[idx] = nums[idx]
        end = mid + 1
        for idx in range(lo, mid + 1):
            while end <= hi and nums[idx] > nums[end] * 2:
                end += 1
            # mid+1实际上是end的初始位置，计算的是delta end
            self.count += end - (mid + 1)
        i, j = lo, mid + 1
        for idx in range(lo, hi + 1):
            if i == mid + 1:
                nums[idx] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[idx] = self.temp[i]
                i += 1
            elif self.temp[i] <= self.temp[j]:
                nums[idx] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[idx] = self.temp[j]
                j += 1


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        merge = Merge()
        merge.sort(nums)
        return merge.count


# @lc code=end
