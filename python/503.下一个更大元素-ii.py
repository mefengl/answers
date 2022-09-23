#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    # 模拟循环数组
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        res = [-1] * len_nums
        # 单调栈的生成方式便是「下一个」更大的数，那将数组本身放在数组的「下一个」即可
        # 模拟的方式揭示了，单调栈的成功运行，需要确保「下一些元素逆序提前入栈」，这样弹出的总是最近的更大元素，也就是下一个更大元素
        stack = []
        for idx in reversed(range(len_nums * 2)):
            idx %= len_nums
            while stack and stack[-1] <= nums[idx]:
                stack.pop()
            if stack:  # has element
                res[idx] = stack[-1]
            stack.append(nums[idx])
        return res

    # # 建立新数组
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     len_nums = len(nums)
    #     res = [-1] * len_nums
    #     # 单调栈的生成方式便是「下一个」更大的数，那将数组本身放在数组的「下一个」即可
    #     circle_nums = nums * 2
    #     stack = []
    #     for idx in reversed(range(len(circle_nums))):
    #         while stack and stack[-1] <= circle_nums[idx]:
    #             stack.pop()
    #         if stack and idx < len_nums:
    #             res[idx] = stack[-1]
    #         stack.append(circle_nums[idx])
    #     return res


# @lc code=end
