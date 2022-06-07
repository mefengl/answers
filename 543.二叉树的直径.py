#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def maxDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.maxDiameter = max(self.maxDiameter, left + right)
            return max(left,right) + 1
        maxDepth(root)
        return self.maxDiameter

# @lc code=end
