#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second = None, None
        self.prev = TreeNode(float("-inf"))

        def inorderTraverse(root: Optional[TreeNode]) -> None:
            global first, second, prev
            if root is None:
                return
            inorderTraverse(root.left)
            if root.val < self.prev.val:
                # 之所以判断是否为None，因为题说恰好一对错误，那么需要找的实际上是第一个和最后一个，None保证first为第一个
                if self.first is None:
                    self.first = self.prev
                self.second = root
            self.prev = root
            inorderTraverse(root.right)

        inorderTraverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val


# @lc code=end
