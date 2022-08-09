#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0]*n
        for booking in bookings:
            i, j, k = booking
            seats[i-1] += k
            if j >= n:
                continue
            seats[j] -= k
        for idx in range(n):
            if idx == 0:
                continue
            seats[idx] += seats[idx-1]
        return seats

# @lc code=end
