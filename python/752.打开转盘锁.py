#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
import collections
from typing import List


# @lc code=start
def up_one(cur, i):
    cur = cur.copy()
    if cur[i] == 9:
        cur[i] = 0
    else:
        cur[i] += 1
    return cur


def down_one(cur, i):
    cur = cur.copy()
    if cur[i] == 0:
        cur[i] = 9
    else:
        cur[i] -= 1
    return cur


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set([tuple([int(x) for x in deadend]) for deadend in deadends])
        target = [int(x) for x in target]
        q = collections.deque([[0, 0, 0, 0]])
        count = 0
        while q:
            # 判断时还没有按按钮，所以不能在这里更新
            # count += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return count
                if tuple(cur) in deadends:
                    continue
                deadends.add(tuple(cur))
                for i in range(4):
                    q.append(up_one(cur, i))
                    q.append(down_one(cur, i))
            count += 1
        return -1


# if __name__ == "__main__":
#     Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
# @lc code=end
