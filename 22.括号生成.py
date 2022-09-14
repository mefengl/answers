#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
def back_track(left, right, path: List[str], res):
    if left == 0 == right == 0:
        res.append("".join(path))
    # 总是先用左括号，所以左括号不可能多于右括号
    if left > right:
        return
    if left < 0 or right < 0:
        return
    path.append("(")
    back_track(left - 1, right, path, res)
    path.pop()
    path.append(")")
    back_track(left, right - 1, path, res)
    path.pop()


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        back_track(n, n, [], res)
        return res


# @lc code=end
