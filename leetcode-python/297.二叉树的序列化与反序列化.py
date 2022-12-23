#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 后序，可以用上pop，但反序列化需要先右后左，先序的话可以reverse再先左后右
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#,"
        # # 后序
        # return self.serialize(root.left)+self.serialize(root.right)+str(root.val)+','
        # 先序
        return (
            str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)
        )

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # # 后序
        # arr = list( filter(None,data.split(',')) )
        # 先序
        arr = list(reversed(list(filter(None, data.split(",")))))
        return self.my_deserialize(arr)

    def my_deserialize(self, arr):
        while arr:
            res = arr.pop()
            if res == "#":
                return None
            root = TreeNode(res)
            # # 后序，先右后左
            # root.right = self.my_deserialize(arr)
            # root.left = self.my_deserialize(arr)
            # 先序，先左后右
            root.left = self.my_deserialize(arr)
            root.right = self.my_deserialize(arr)

            return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
