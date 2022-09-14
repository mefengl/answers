#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start


def swap(cur, i, j):
    cur[i], cur[j] = cur[j], cur[i]
    return "".join(cur)


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbor = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        q = collections.deque()
        line = [-1] * 6
        for i in range(6):
            line[i] = str(board[i // 3][i % 3])
            if line[i] == 0:
                zero_index = i
        visited = set()
        q.append("".join(line))
        count = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == "123450":
                    return count
                if cur in visited:
                    continue
                visited.add(cur)
                zero_index = cur.index("0")
                for i in neighbor[zero_index]:
                    q.append(swap(list(cur), zero_index, i))
            count += 1
        return -1


# @lc code=end
