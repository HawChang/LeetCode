#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        inf = 1000

        dp = [[inf for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][1] = 0
        dp[1][0] = 0
        
        for cur_row in range(1, m + 1):
            for cur_col in range(1, n + 1):
                dp[cur_row][cur_col] = grid[cur_row - 1][cur_col - 1] + \
                        min(dp[cur_row - 1][cur_col], dp[cur_row][cur_col - 1])
        
        print("dp: {}".format(dp))
        
        return dp[m][n]


# @lc code=end

