#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # 层遍历
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return root
        q = deque([root])
        while q:
            lenq = len(q)
            for idx in range(lenq):
                n = q.popleft()
                if idx < lenq - 1:
                    n.next = q[0]
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
        return root


# @lc code=end
