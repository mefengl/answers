#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        prefix = []
        for num in nums:
            if (num - 1) in prefix:
                prefix.remove(num - 1)
                prefix.append(num)
            else:
                # 看是否可能三连对
                if count[num + 1] > 0 and count[num + 2] > 0:
                    count[num + 1] -= 1
                    count[num + 2] -= 1
                    prefix.append(num)
                else:
                    return False
        return True


# @lc code=end
