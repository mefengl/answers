#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 完全二叉树：子树是满二叉树用满二叉树，子树是普通树用纯遍历
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        l = r = root
        hl,hr = 0,0
        while l is not None:
            hl += 1
            l = l.left
        while r is not None:
            hr += 1
            r = r.right
        if hl == hr:
            return 2**hl - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# # 纯遍历
# class Solution:
#     def traverse(self,root):
#         if root is None: return 0
#         return 1 + self.traverse(root.left) + self.traverse(root.right)
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         return self.traverse(root)

# # 满二叉树
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         h = 0
#         while root is not None:
#             h += 1
#             root = root.left
#         return 2 ** h - 1

# @lc code=end
