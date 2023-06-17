#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

# @lc code=start


class Solution:
    def __init__(self, nums: List[int]):
        self._dict = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            self._dict[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self._dict[target])


# # 蓄水池抽样（超时）
# class Solution:
#     def __init__(self, nums: List[int]):
#         self._nums = nums

#     def pick(self, target: int) -> int:
#         res = 0
#         visited_num = 0
#         for idx, num in enumerate(self._nums):
#             if num == target:
#                 visited_num += 1
#                 if randrange(visited_num) == 0:  # 1/visited_num 的概率
#                     res = idx
#         return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
