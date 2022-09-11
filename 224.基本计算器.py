#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
def by_op(a: int, b: int, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b


class Solution:
    def calculate(self, s: str) -> int:
        # 去除空格
        s = s.replace(" ", "")
        # 单元运算补全
        s = "(" + s + ")"
        s = s.replace("(-", "(0-")

        nums = []
        ops = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                ops.append(s[i])
            elif s[i] == ")":
                while ops:
                    op = ops.pop()
                    if op == "(":
                        break
                    b, a = nums.pop(), nums.pop()
                    nums.append(by_op(a, b, op))
            elif "0" <= s[i] <= "9":
                num = 0
                while i < len(s) and "0" <= s[i] <= "9":
                    num = num * 10 + (ord(s[i]) - ord("0"))
                    i += 1
                # 因为后面会统一+
                i -= 1
                nums.append(num)
            else:
                while ops and ops[-1] != "(":
                    b, a = nums.pop(), nums.pop()
                    nums.append(by_op(a, b, ops.pop()))
                ops.append(s[i])
            i += 1
        while ops:
            b, a = nums.pop(), nums.pop()
            nums.append(by_op(a, b, ops.pop()))
        return nums[0]


# if __name__ == "__main__":
#     S = Solution()
#     S.calculate("1-(     -2)")

# @lc code=end
