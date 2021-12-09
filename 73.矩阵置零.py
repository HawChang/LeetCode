#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_zero = False
        # 记录每行每列的情况
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                first_row_has_zero = True
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # 根据第一行和第一列 更新
        # 但不能马上更新第一行 所以从最后一行往前更新 最后更新第一行
        for row in range(len(matrix)-1, -1, -1):
            for col in range(1, len(matrix[row])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if first_row_has_zero:
                matrix[row][0] = 0


# @lc code=end

