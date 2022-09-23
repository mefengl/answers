#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # # 最近公共祖先+二叉搜索
    # def find(self,root,val1,val2):
    #     if root is None: return None
    #     if root.val == val1 or root.val == val2:
    #         return root
    #     if root.val < val1:
    #         left = None
    #     else:
    #         left = self.find(root.left,val1,val2)
    #     if root.val > val2:
    #         right = None
    #     else:
    #         right = self.find(root.right,val1,val2)
    #     if left is not None and right is not None: return root
    #     return left if left is not None else right

    # 二叉搜索+最近公共祖先
    def find(self, root, val1, val2):
        if root is None:
            return None
        if root.val > val2:
            return self.find(root.left, val1, val2)
        elif root.val < val1:
            return self.find(root.right, val1, val2)
        elif val1 <= root.val <= val2:
            return root

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # ensure p.val <= q.val
        if p.val > q.val:
            p, q = q, p
        return self.find(root, p.val, q.val)


# @lc code=end
