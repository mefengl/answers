#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, lo: int, hi: int) -> List[Optional[TreeNode]]:
        res = []
        if lo > hi:
            res.append(None)
            return res
        for mid in range(lo, hi + 1):
            lefts = self.build(lo, mid - 1)
            rights = self.build(mid + 1, hi)
            for left in lefts:
                for right in rights:
                    root = TreeNode(mid)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.build(1, n)


# @lc code=end
