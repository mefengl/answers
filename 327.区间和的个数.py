#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#

# @lc code=start
class Merge:
    def __init__(self,lower,upper):
        self.temp = []
        self.count = 0
        self.lower = lower
        self.upper = upper
    def sort(self,nums):
        lennums = len(nums)
        self.temp=[0]*lennums
        self._sort(nums,0,lennums-1)
    def _sort(self,nums,lo,hi):
        if lo == hi:
            return
        mid = lo+(hi-lo)//2
        self._sort(nums,lo,mid)
        self._sort(nums,mid+1,hi)
        self.merge(nums,lo,mid,hi)
    def merge(self,nums,lo,mid,hi):
        for idx in range(lo,hi+1):
            self.temp[idx] = nums[idx]
        start=end=mid+1
        for idx in range(lo,mid+1):
            # end = 满足(xx,end]的数目, start = 满足(xx,start)的数目
            # end-start = 满足[start,end]的数目
            while start <= hi and nums[start] - nums[idx] < self.lower:
                start+=1
            while end <= hi and nums[end] - nums[idx] <= self.upper:
                end+=1
            self.count+=end-start

        i,j = lo,mid+1
        for idx in range(lo,hi+1):
            if i == mid+1:
                nums[idx] = self.temp[j]
                j +=1
            elif j == hi+1:
                nums[idx] = self.temp[i]
                i +=1
            elif self.temp[i] <= self.temp[j]:
                nums[idx] = self.temp[i]
                i +=1
            elif self.temp[i] > self.temp[j]:
                nums[idx] = self.temp[j]
                j +=1

class Solution:
    def preSum(self,nums: List[int])->List[int]:
        lennums = len(nums)
        res = [0]*(lennums+1)
        for idx in range(lennums):
            res[idx+1] = nums[idx] + res[idx]
        return res
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = self.preSum(nums)
        merge = Merge(lower,upper)
        merge.sort(presum)
        return merge.count

# @lc code=end
