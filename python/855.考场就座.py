#
# @lc app=leetcode.cn id=855 lang=python3
#
# [855] 考场就座
#
# @lc code=start


class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.start = {}
        self.end = {}
        self.pq = []
        self.add_interval([-1, n])

    def distance(self, interval: List[int]) -> int:
        x, y = interval
        n = self.n
        if x == -1:
            return y
        if y == n:
            return n - 1 - x
        return (y - x) // 2

    def add_interval(self, interval: List[int]) -> None:
        # 以线段长度排序，负号用于逆序
        self.pq.append([-self.distance(interval)] + interval)
        self.start[interval[0]] = interval
        self.end[interval[1]] = interval

    def remove_interval(self, interval: List[int]) -> None:
        self.pq.remove([-self.distance(interval)] + interval)
        self.start.pop(interval[0])
        self.end.pop(interval[1])

    def seat(self) -> int:
        # TODO 实现真正的优先队列
        longest = sorted(self.pq)[0]

        _, x, y = longest
        seat = 0
        if x == -1:
            # 第一位学生做最前面
            seat = 0
        elif y == self.n:
            # 第二位做最后
            seat = self.n - 1
        else:
            # 坐在最长空段的中间
            seat = (y - x) // 2 + x
        self.remove_interval(longest[1:])
        self.add_interval([x, seat])
        self.add_interval([seat, y])
        return seat

    def leave(self, p: int) -> None:
        # 以 p start的是右边，end的是左边
        right, left = self.start[p], self.end[p]
        self.remove_interval(left)
        self.remove_interval(right)
        self.add_interval([left[0], right[1]])


# if __name__ == "__main__":
#     ER = ExamRoom(10)
#     ER.seat()
#     ER.seat()
#     ER.seat()
#     ER.leave(0)
#     ER.leave(4)
#     # 5
#     ER.seat()
#     ER.seat()
#     ER.seat()
#     ER.seat()
#     ER.seat()
#     # 4
#     ER.seat()
#     ER.seat()
#     ER.seat()
#     ER.seat()
#     # 1
#     ER.leave(0)
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end
