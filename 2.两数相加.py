#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode()
        p = dummy
        carry = 0
        while p1 != None or p2 != None or carry > 0:
            val = carry
            if p1 != None:
                val += p1.val
                p1 = p1.next
            if p2 != None:
                val += p2.val
                p2 = p2.next
            carry = val//10
            p.next = ListNode(val % 10)
            p = p.next
        return dummy.next
# @lc code=end
