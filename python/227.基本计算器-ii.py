#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
def calc(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b


class Solution:
    order = {"+": 1, "-": 1, "*": 2, "/": 2}

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = "(" + s + ")"
        s = s.replace("(-", "(0-")

        nums, ops = [], []
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
                    num = num * 10 + (ord(s[i]) - ord("0"))
                    i += 1
                nums.append(num)
                i -= 1
            else:
                # 和遇到")"不同的是，只停止运算，不弹出"("
                while ops and ops[-1] != "(":
                    # 下一步运算优先级不够的情况下，停止运算
                    if self.order[ops[-1]] < self.order[s[i]]:
                        break
                    op = ops.pop()
                    b, a = nums.pop(), nums.pop()
                    nums.append(calc(a, b, op))
                ops.append(s[i])
            i += 1
        while ops:
            op = ops.pop()
            b, a = nums.pop(), nums.pop()
            nums.append(calc(a, b, op))
        return nums[0]


# if __name__ == "__main__":
#     S = Solution()
#     S.calculate("3+2*2")
# @lc code=end
