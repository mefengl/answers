#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        s = f = head
        while f is not None:
            if s.val != f.val:
                s.next = f
                # s需要移动到下个宿主元素(反正要被替代，不重要，只要不是当前这个就可以)
                s = s.next
            f = f.next
        # 和数组不同，需要断开其它宿主元素
        s.next = None
        return head
# @lc code=end
