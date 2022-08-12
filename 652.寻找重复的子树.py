#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        mymap = {}
        def serialize(node):
            if not node: return '#'
            subtree = str(node.val)+','+serialize(node.left)+','+serialize(node.right)
            if subtree not in mymap:
                mymap[subtree] = 1
            elif mymap[subtree] == 1:
                res.append(node)
                mymap[subtree] += 1
            return subtree
        serialize(root)
        return res


# @lc code=end
