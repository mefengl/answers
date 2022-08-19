#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 这一步很重要，in List是O(n)，in set是O(1)
        if target == "0000":
            return 0
        visited = set(deadends)
        q = deque(["0000"])
        q2 = deque([target])
        # 同上，没这步，双向BFS是负优化（1700ms）
        temp = set()
        step = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur in temp:
                    return step
                if cur in visited:
                    continue
                cur = [x for x in cur]
                visited.add("".join(cur))
                for idx in range(len(cur)):
                    upcur = "".join(
                        [
                            str((int(cur[idx]) + 1) % 10) if i == idx else cur[i]
                            for i in range(len(cur))
                        ]
                    )
                    downcur = "".join(
                        [
                            str((int(cur[idx]) - 1) % 10) if i == idx else cur[i]
                            for i in range(len(cur))
                        ]
                    )
                    q.append(upcur)
                    q.append(downcur)
            step += 1
            # 双向BFS，从1200ms到200ms
            q, q2 = q2, q
            temp = set(q2)
        return -1


# @lc code=end
