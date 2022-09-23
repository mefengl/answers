#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float("-inf")

    def oneSideSum(self, root):
        if root is None:
            return 0
        left = max(0, self.oneSideSum(root.left))
        right = max(0, self.oneSideSum(root.right))
        self.res = max(self.res, root.val + left + right)
        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.oneSideSum(root)
        return self.res


# @lc code=end
