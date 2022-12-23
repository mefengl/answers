#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:
    def __init__(self):
        self._queue = collections.deque()
        self._top_value = 0

    def push(self, x: int) -> None:
        self._queue.append(x)
        self._top_value = x

    def pop(self) -> int:
        q = self._queue
        len_q = len(q)
        while len_q > 2:
            q.append(q.popleft())
            len_q -= 1
        # 离old_top最近的左元素，会最晚被popleft，所以如果只剩两个元素，那么new_top正在top上等待被pop
        self._top_value = q[0]
        # pop new_top to tail
        q.append(q.popleft())
        return q.popleft()

    def top(self) -> int:
        return self._top_value

    def empty(self) -> bool:
        return not self._queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
