#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        max_edge = 0

        for cur_row in range(1, row + 1):
            for cur_col in range(1, col + 1):
                if matrix[cur_row - 1][cur_col - 1] == '0':
                    dp[cur_row][cur_col] = 0
                else:
                    cur_edge = min(dp[cur_row - 1][cur_col - 1], dp[cur_row][cur_col - 1], dp[cur_row - 1][cur_col]) + 1
                    dp[cur_row][cur_col] = cur_edge
                    if cur_edge > max_edge:
                        max_edge = cur_edge
                
        return max_edge ** 2


# @lc code=end

