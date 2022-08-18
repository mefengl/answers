#
# @lc app=leetcode.cn id=1650 lang=python3
#
# [1650] 二叉树的最近公共祖先 III
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a,b = p,q
        while a != b:
            if a is None:
                a = q
            else:
                a = a.parent
            if b is None: 
                b = p
            else:
                b = b.parent
        return a
        
# @lc code=end
