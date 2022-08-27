#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self._head_stack = []
        self._tail_stack = []

    def push(self, x: int) -> None:
        self._tail_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self._head_stack.pop()

    def peek(self) -> int:
        head, tail = self._head_stack, self._tail_stack
        if not head:  # empty
            while tail:
                head.append(tail.pop())
        # tail_stack的pop是最后一个元素，不是0，因为在 ] [ 中，tail是倒置的
        return head[-1]

    def empty(self) -> bool:
        head, tail = self._head_stack, self._tail_stack
        if head:
            return False
        if tail:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
