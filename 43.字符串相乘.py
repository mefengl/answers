#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
def to_num(char: str):
    return ord(char) - ord("0")


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i = j = 0
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2)
        for i in reversed(range(len1)):
            for j in reversed(range(len2)):
                mul = to_num(num1[i]) * to_num(num2[j])
                p = i + j + 1
                _sum = mul + res[p]
                # 低位
                res[p] = _sum % 10
                # 高位
                res[p - 1] += _sum // 10
        res = "".join([str(x) for x in res])
        # 0000000的情况，0123的情况
        while len(res) > 1 and res[0] == "0":
            res = res[1:]
        return res


# @lc code=end
