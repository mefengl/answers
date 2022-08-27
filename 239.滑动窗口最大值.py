#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class MonotonicQueue:
    def __init__(self):
        self._queue = collections.deque()

    def put(self, n: int):
        q = self._queue
        while q and q[-1] < n:
            q.pop()
        q.append(n)

    def max(self):
        return self._queue[0]

    def pop(self, n: int):
        q = self._queue
        # idx_n=idx-k+1，即理论上的窗口开始的索引，如果已经被「压出去」，那么什么也不做
        if q[0] != n:
            return
        return self._queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []
        for idx, num in enumerate(nums):
            if idx < k - 1:  # 0到k-2，也就是k-1个
                window.put(num)
            else:
                window.put(num)  # 窗口补齐
                res.append(window.max())
                # idx_n=idx-k+1，即理论上的窗口开始的索引，如果已经被「压出去」，那么什么也不做
                window.pop(nums[idx - k + 1])
        return res


# @lc code=end
