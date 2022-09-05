#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
def flip(array: List) -> List:
    return list(reversed(array))


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 因为需要反向遍历
        dungeon = flip([flip(x) for x in dungeon])
        dp = [x.copy() for x in dungeon]
        # 根据最小生命值的定义确定初始值
        if dp[0][0] <= 0:
            dp[0][0] = -dungeon[0][0] + 1
        else:
            dp[0][0] = 1
        for i, _ in enumerate(dp):
            for j, _ in enumerate(dp[0]):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] - dungeon[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] - dungeon[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) - dungeon[i][j]
                if dp[i][j] <= 0:
                    dp[i][j] = 1
        return dp[-1][-1]


# @lc code=end
