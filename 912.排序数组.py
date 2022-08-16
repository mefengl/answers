#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Merge:
    temp = []
    def sort(self,nums):
        self.temp = nums.copy()
        self._sort(nums,0,len(nums)-1)
    def _sort(self,nums,lo,hi):
        if lo==hi:
            return
        mid = (hi-lo)//2+lo
        self._sort(nums,lo,mid)
        self._sort(nums,mid+1,hi)
        self.merge(nums,lo,mid,hi)

    def merge(self,nums,lo,mid,hi):
        for idx in range(lo,hi+1):
            self.temp[idx] = nums[idx]
        i,j = lo,mid+1
        for idx in range(lo,hi+1):
            if i == mid+1:
                nums[idx] = self.temp[j]
                j+=1
            elif j == hi+1:
                nums[idx] = self.temp[i]
                i+=1
            elif self.temp[i] >= self.temp[j]:
                nums[idx] = self.temp[j]
                j+=1
            elif self.temp[i] < self.temp[j]:
                nums[idx] = self.temp[i]
                i+=1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge = Merge()
        merge.sort(nums)
        return nums

# @lc code=end
