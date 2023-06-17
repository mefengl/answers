#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        for idx in range(2, int(math.sqrt(n)) + 1):
            if is_prime[idx]:
                for false_idx in range(idx * idx, n, idx):
                    is_prime[false_idx] = False
        # 切片用于忽略0和1
        return sum(is_prime[2:])


# @lc code=end
