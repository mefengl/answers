#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # # 回溯
    # max = 0
    # cur = 0
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     if self.cur > self.max:
    #         self.max = self.cur
    #     self.cur += 1
    #     self.maxDepth(root.left)
    #     self.cur -= 1
    #     self.cur += 1
    #     self.maxDepth(root.right)
    #     self.cur -= 1
    #     return self.max+1


# @lc code=end
