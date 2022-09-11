#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r_need = 0
        res = 0
        for c in s:
            if c == "(":
                r_need += 1
            elif c == ")":
                r_need -= 1
                # 右括号过多，这里就需要插入，不然会和多余的左括号抵消
                if r_need == -1:
                    r_need += 1
                    # 一次插入
                    res += 1
        return res + r_need


# @lc code=end
