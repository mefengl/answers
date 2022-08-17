#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge = Merge()
        # merge.sort(nums)
        quick = Quick()
        quick.sort(nums)
        return nums

# # 归并排序
# class Merge:
#     temp = []
#     def sort(self,nums):
#         self.temp = nums.copy()
#         self._sort(nums,0,len(nums)-1)
#     def _sort(self,nums,lo,hi):
#         if lo==hi:
#             return
#         mid = (hi-lo)//2+lo
#         self._sort(nums,lo,mid)
#         self._sort(nums,mid+1,hi)
#         self.merge(nums,lo,mid,hi)

#     def merge(self,nums,lo,mid,hi):
#         for idx in range(lo,hi+1):
#             self.temp[idx] = nums[idx]
#         i,j = lo,mid+1
#         for idx in range(lo,hi+1):
#             if i == mid+1:
#                 nums[idx] = self.temp[j]
#                 j+=1
#             elif j == hi+1:
#                 nums[idx] = self.temp[i]
#                 i+=1
#             elif self.temp[i] >= self.temp[j]:
#                 nums[idx] = self.temp[j]
#                 j+=1
#             elif self.temp[i] < self.temp[j]:
#                 nums[idx] = self.temp[i]
#                 i+=1

# 快速排序
class Quick:
    def sort(self,nums):
        # self.shuffle(nums)
        random.shuffle(nums)
        self._sort(nums,0,len(nums)-1)

    def _sort(self,nums,lo,hi):
        if lo >= hi:
            return
        p = self.partition(nums,lo,hi)
        self._sort(nums,lo,p-1)
        self._sort(nums,p+1,hi)
    
    def partition(self,nums,lo,hi):
        pivot = nums[lo]
        i,j = lo+1, hi
        while i <= j:
            while i < hi and nums[i] <= pivot:
                i += 1
            while j > lo and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i],nums[j] = nums[j],nums[i]
        # j是小于等于，i是一定大于，j在i前，所以换j
        nums[lo],nums[j] = nums[j],nums[lo]
        return j
    def shuffle(self,nums):
        lennums = len(nums)
        for idx in range(lennums):
            randomidx = random.randint(0,lennums-1)
            nums[idx],nums[randomidx] = nums[randomidx],nums[idx]


# @lc code=end
