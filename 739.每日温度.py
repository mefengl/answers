#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        len_temperatures = len(temperatures)
        res = [0] * len(temperatures)
        for idx in reversed(range(len_temperatures)):
            while stack and temperatures[stack[-1]] <= temperatures[idx]:
                stack.pop()
            if stack:
                res[idx] = stack[-1] - idx
            stack.append(idx)
        return res


# @lc code=end
