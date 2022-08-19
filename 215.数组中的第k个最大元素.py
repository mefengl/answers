#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def shuffle(self, nums):
        lennums = len(nums)
        for idx in range(lennums):
            randidx = random.randint(0, lennums - 1)
            nums[randidx], nums[idx] = nums[idx], nums[randidx]

    def partition(self, nums, lo, hi):
        pivot = nums[lo]
        i, j = lo + 1, hi
        while True:
            while i < hi and nums[i] <= pivot:
                i += 1
            while j > lo and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            self.swap(nums, i, j)
        self.swap(nums, lo, j)
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        lennums = len(nums)
        self.shuffle(nums)
        lo, hi = 0, lennums - 1
        # 因为是数组，可知长度，所以第K大只是表示一种大小关系，也可以转化为第K'小，从而转化为数组中的序号
        k = lennums - k
        while lo <= hi:
            p = self.partition(nums, lo, hi)
            if p < k:
                lo = p + 1
            elif p > k:
                hi = p - 1
            elif p == k:
                return nums[p]
        return -1


# @lc code=end
