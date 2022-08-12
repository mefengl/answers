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

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node is None:
                res+='#,'
                continue
            res+=str(node.val)+','
            q.append(node.left)
            q.append(node.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = list(filter(None, data.split(',')))
        return self.my_deserialize(arr)
    def my_deserialize(self,arr):
        if arr[0] == '#':
            return None
        root = TreeNode( arr[0] )
        q = collections.deque([root])
        i = 1
        while i < len(arr):
            parent = q.popleft()
            left = arr[i]
            i+=1
            if left == '#':
                parent.left = None
            else:
                leftChild = TreeNode(left)
                parent.left = leftChild
                q.append(leftChild)
            right = arr[i]
            i+=1
            if right == '#':
                parent.right = None
            else:
                rightChild = TreeNode(right)
                parent.right = rightChild
                q.append(rightChild)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
