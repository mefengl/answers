#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
def build_greater_list(nums: int):
    len_nums = len(nums)
    res = [0] * len(nums)
    stack = []
    for idx in reversed(range(len_nums)):
        while stack and stack[-1] <= nums[idx]:
            stack.pop()
        if not stack:  # stack为空
            res[idx] = -1
        else:
            # 不比较，不用弹出
            res[idx] = stack[-1]
        stack.append(nums[idx])
    return res


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_list = build_greater_list(nums2)
        greater_map = {num: idx for idx, num in enumerate(nums2)}
        for idx, num in enumerate(nums1):
            nums1[idx] = greater_list[greater_map[num]]
        return nums1


# @lc code=end
