#
# @lc app=leetcode.cn id=1541 lang=python3
#
# [1541] 平衡括号字符串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        r_need = 0
        res = 0
        for c in s:
            if c == "(":
                # 在承认左括号之前，要检查左括号前面的左右括号是否可能平衡，因为在此左括号后的右括号，已经不能补全前面如果右括号为单数的问题了
                if r_need % 2 == 1:
                    r_need -= 1
                    res += 1
                r_need += 2
            elif c == ")":
                r_need -= 1
                # 插入左括号，但此时右括号需求加2
                if r_need == -1:
                    r_need += 2
                    res += 1
        return res + r_need


# @lc code=end
