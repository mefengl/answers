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


from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([root])
        step = 1
        while q:
            # 控制step随层数而加
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return step

                def put(node):
                    if node:
                        q.append(node)
                put(cur.left)
                put(cur.right)
            step += 1
        return -1


# @lc code=end
