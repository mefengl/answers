#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start
class Solution:
    class Pair:
        def __init__(self,val,id):
            self.val = val
            self.id = id
    def __init__(self):
        self.temp = []
        self.count = []
    def countSmaller(self, nums: List[int]) -> List[int]:
        lennums = len(nums)
        self.count = [0]*lennums
        self.temp = [None]*lennums
        arr = [None]*lennums
        for idx,num in enumerate(nums):
            arr[idx] = self.Pair(num,idx)
        self.sort(arr, 0, lennums-1)
        return self.count

    def sort(self,arr,lo,hi):
        if lo == hi:
            return
        mid = lo+(hi-lo)//2
        self.sort(arr,lo,mid)
        self.sort(arr,mid+1,hi)
        self.merge(arr,lo,mid,hi)

    def merge(self,arr,lo,mid,hi):
        for idx in range(lo,hi+1):
            self.temp[idx] = arr[idx]
        i,j = lo,mid+1
        for idx in range(lo,hi+1):
            if i == mid+1:
                arr[idx] = self.temp[j]
                j+=1
            elif j == hi+1:
                arr[idx] = self.temp[i]
                i+=1
                self.count[arr[idx].id] += j - mid - 1
            elif self.temp[i].val<=self.temp[j].val:
                arr[idx] = self.temp[i]
                i+=1
                self.count[arr[idx].id] += j - mid - 1
            elif self.temp[i].val>self.temp[j].val:
                arr[idx] = self.temp[j]
                j+=1



        
# @lc code=end
