#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self._head = head

    def getRandom(self) -> int:
        res = 0
        node = self._head
        visited_num = 0
        while node is not None:
            visited_num += 1
            if 0 == randrange(visited_num):
                res = node.val
            node = node.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
