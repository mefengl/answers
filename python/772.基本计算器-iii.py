#
# @lc app=leetcode.cn id=772 lang=python3
#
# [772] 基本计算器 III
#

# @lc code=start
def calc(a: int, b: int, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if a ^ b < 0:  # 负数
            return -(abs(a) // abs(b))
        return a // b


def to_num(char: str) -> int:
    return ord(char) - ord("0")


class Solution:
    order = {"+": 1, "-": 1, "*": 2, "/": 2}

    def calculate(self, s: str) -> int:
        s = "(" + s + ")"
        # 去除空格和添加单元运算符的0
        s = s.replace(" ", "").replace("(-", "(0-")

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
                    nums.append(calc(a, b, op))
            elif "0" <= s[i] <= "9":
                num = 0
                while i < len(s) and "0" <= s[i] <= "9":
                    num = num * 10 + to_num(s[i])
                    i += 1
                nums.append(num)
                i -= 1
            else:
                while ops and ops[-1] != "(":
                    o = self.order
                    if o[ops[-1]] < o[s[i]]:
                        break
                    b, a = nums.pop(), nums.pop()
                    nums.append(calc(a, b, ops.pop()))
                # 勿忘
                ops.append(s[i])
            i += 1
        while ops:
            b, a = num.pop(), num.pop()
            nums.append(calc(a, b, ops.pop()))
        return nums[0]


# if __name__ == "__main__":
#     S = Solution()
#     S.calculate("1+1")
# @lc code=end
