#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#

# @lc code=start
MAX_VALUE = 2**32


def trailing_zeros(n: int) -> int:
    res = 0
    divisor = 5
    while divisor <= n:
        res += n // divisor
        divisor *= 5
    return res


# 第一个满足条件的数
def left_bound(target: int) -> int:
    left, right = 0, MAX_VALUE
    while left <= right:
        mid = left + (right - left) // 2
        mid_zeros = trailing_zeros(mid)
        if mid_zeros < target:
            left = mid + 1
        elif mid_zeros > target:
            right = mid - 1
        elif mid_zeros == target:
            right = mid - 1
        print(left, right)
    return left


# 最后一个满足条件的数
def right_bound(target: int) -> int:
    left, right = 0, MAX_VALUE
    while left <= right:
        mid = left + (right - left) // 2
        mid_zeros = trailing_zeros(mid)
        if mid_zeros < target:
            left = mid + 1
        elif mid_zeros > target:
            right = mid - 1
        elif mid_zeros == target:
            left = mid + 1
        print(left, right)
    return right


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        return right_bound(k) - left_bound(k) + 1


# @lc code=end
