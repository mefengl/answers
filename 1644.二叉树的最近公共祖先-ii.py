#
# @lc app=leetcode.cn id=1644 lang=python3
#
# [1644] 二叉树的最近公共祖先 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.foundP = False
        self.foundQ = False
    def find(self,root:TreeNode,val1:int,val2:int):
        if root is None: return None
        left = self.find(root.left,val1,val2)
        right = self.find(root.right,val1,val2)
        # 两个都有，排除了不存在的可能，直接返回
        if left is not None and right is not None:
            return root
        
        if root.val == val1: 
            self.foundP = True
            return root
        if root.val == val2: 
            self.foundQ = True
            return root

        return left if left is not None else right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = self.find(root,p.val,q.val)
        is_found = self.foundP and self.foundQ
        return res if is_found else None
        
# @lc code=end
