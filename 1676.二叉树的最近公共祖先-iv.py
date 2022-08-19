#
# @lc app=leetcode.cn id=1676 lang=python3
#
# [1676] 二叉树的最近公共祖先 IV
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def find(self, root: TreeNode, nodes: List[TreeNode]):
        if root is None:
            return None
        if root in nodes:
            return root
        left = self.find(root.left, nodes)
        right = self.find(root.right, nodes)
        if left is not None and right is not None:
            return root
        return left if left is not None else right

    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        return self.find(root, nodes)


# @lc code=end
