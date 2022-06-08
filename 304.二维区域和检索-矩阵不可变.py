#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        leni = len(matrix)+1
        lenj = len(matrix[0])+1
        presum = [[0]*lenj for _ in range(leni)]
        for i in range(1, leni):
            for j in range(1, lenj):
                presum[i][j] = presum[i-1][j]+presum[i][j-1] - \
                    presum[i-1][j-1]+matrix[i-1][j-1]
        self.presum = presum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
        presum = self.presum
        # 处于右下的row和col总要+1，这是由row包围的定义决定的
        return presum[row2+1][col2+1]-presum[row1][col2+1]-presum[row2+1][col1]+presum[row1][col1]
        # @lc code=end
