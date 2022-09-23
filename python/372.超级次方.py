#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
BASE = 1337


def my_pow(a: int, k: int) -> int:
    # 两个数乘积的模，等于两个数的模的乘积再取模，a取模，则求a的幂时，各个乘数都取了模
    if k == 0:
        return 1
    a %= BASE
    # a^k = a^(k-1) * a
    if k % 2 == 1:  # 奇数
        return a * my_pow(a, k - 1) % BASE
    # a^k = (a^(k/2))^2
    elif k % 2 == 0:  # 偶数
        return my_pow(a, k // 2) ** 2 % BASE


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()

        # a^[1,2,3] = a^3 * a^[1,2,0] = a^3 * (a^[1,2])^10
        part1 = my_pow(a, last)
        part12 = my_pow(self.superPow(a, b), 10)
        return part1 * part12 % BASE


# @lc code=end
