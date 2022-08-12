#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxidx(self,nums):
        return nums.index(max(nums))
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode(max(nums))
        maxidx = self.maxidx(nums)
        root.left = self.constructMaximumBinaryTree(nums[:maxidx])
        root.right = self.constructMaximumBinaryTree(nums[maxidx+1:])
        return root
        
# @lc code=end
