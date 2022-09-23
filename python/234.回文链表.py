#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, a, b):
        pre, cur, nxt = None, a, a
        while cur is not b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        # is None 和 is not None的区别真的很小
        # 可能还是!=和==更方便
        # while fast is not None and fast.next is None:
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # 指向后半部分，而不是奇数时的中间
        if fast is not None:
            slow = slow.next
        right = self.reverse(slow, None)
        left = head
        while right is not None:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True


# @lc code=end

# 递归
# class Solution:
#     left = ListNode()

#     def traverse(self, right):
#         if right is None:
#             return True
#         res = self.traverse(right.next)
#         res = res and (self.left.val == right.val)
#         self.left = self.left.next
#         return res

#     def isPalindrome(self, head: ListNode) -> bool:
#         self.left = head
#         return self.traverse(head)
