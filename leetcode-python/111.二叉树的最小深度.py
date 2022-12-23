#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        q = collections.deque([root])
        while q:
            # 每次遍历都是新层
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left == None and node.right == None:
                    return depth
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)


# @lc code=end
