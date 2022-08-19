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

    # 语义清晰版
    maxD = 0

    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDiameter(root):
            if root is None:
                return
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if left + right > self.maxD:
                self.maxD = left + right
            maxDiameter(root.left)
            maxDiameter(root.right)

        maxDiameter(root)
        return self.maxD
        # self.maxDiameter = 0
        # def maxDepth(root: Optional[TreeNode]) -> int:
        #     if root is None:
        #         return 0
        #     left = maxDepth(root.left)
        #     right = maxDepth(root.right)
        #     self.maxDiameter = max(self.maxDiameter, left + right)
        #     return max(left,right) + 1
        # maxDepth(root)
        # return self.maxDiameter


# @lc code=end
