#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode],min: Optional[TreeNode],max:Optional[TreeNode]):
        if root is None: return True
        if min is not None and root.val <= min.val: return False
        if max is not None and root.val >= max.val: return False
        return self.traverse(root.left,min,root) and self.traverse(root.right,root,max)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root,None,None)
# @lc code=end
