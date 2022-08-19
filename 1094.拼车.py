#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seats = [0] * 1000
        for trip in trips:
            k, i, j = trip
            seats[i] += k
            if j >= 1000:
                continue
            seats[j] -= k
        for idx in range(1000):
            if idx != 0:
                seats[idx] += seats[idx - 1]
            if seats[idx] > capacity:
                return False
        return True


# @lc code=end
