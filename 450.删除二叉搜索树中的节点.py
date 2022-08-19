#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxNode(self, root):
        while root.right is not None:
            root = root.right
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # 左子树最大，或右子树里最小，选择前者，矮子里挑将军
            else:
                maxNode = self.maxNode(root.left)
                # 这一步为最妙
                root.left = self.deleteNode(root.left, maxNode.val)
                maxNode.left = root.left
                maxNode.right = root.right
                root = maxNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root


# @lc code=end
