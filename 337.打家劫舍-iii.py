#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def traverse(root: Optional[TreeNode]):
    if root is None:
        return (0, 0)
    left = traverse(root.left)
    right = traverse(root.right)
    # (偷, 不偷)
    # 偷就只能不偷子节点，不偷就能自由选择是否偷子节点
    return (root.val + left[1] + right[1], max(left) + max(right))


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(traverse(root))


# @lc code=end
