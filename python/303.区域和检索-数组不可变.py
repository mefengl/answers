#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        presum = [0] + nums
        for idx in range(len(presum)):
            if idx == 0:
                continue
            presum[idx] += presum[idx - 1]
        self.presum = presum

    def sumRange(self, left: int, right: int) -> int:
        presum = self.presum
        return presum[right + 1] - presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
