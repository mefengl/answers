#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, a, b):
        # None是指空指针，因为反转，pre相当与结尾的空指针
        pre, cur, nxt = None, a, a
        while cur != b:
            # 保存下个节点
            nxt = cur.next
            # 替代指向下个节点的指针到上个节点(下个节点已保存不会丢失)
            cur.next = pre
            # 移动到下一个(情况完全相同)
            pre = cur
            cur = nxt
        # 实际返回的是cur，即b前的元素
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        b = head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        newhead = self.reverse(head, b)
        head.next = self.reverseKGroup(b, k)
        return newhead

        # @lc code=end
