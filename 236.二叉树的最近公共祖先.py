#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def find(self, root: "TreeNode", val1: int, val2: int) -> "TreeNode":
        if root is None:
            return None
        if root.val == val1 or root.val == val2:
            return root
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        if left is not None and right is not None:
            return root
        return left if left is not None else right

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        return self.find(root, p.val, q.val)


# @lc code=end
