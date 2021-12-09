#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 加两个边界球 方便求解
        nums = [1] + nums + [1]

        num_len = len(nums)
        # dp[i][j]：气球i与气球j之间的气球(不包括i和j) 能得到的最多硬币
        # 该问题可以拆解为，最后一次戳的是气球k
        # dp[i][j] = dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j]
        dp = [[0 for _ in range(num_len)] for _ in range(num_len)]

        # 边界问题：
        # dp[i][i] = 0
        # dp[i][i + 1] = 0

        # 正序遍历col
        for cur_col in range(2, num_len):
            # 倒序遍历row
            # 遍历顺序是由状态转移方程决定的
            for cur_row in range(cur_col - 2, -1 , -1):
                cur_max_coin = None
                for cur_mid in range(cur_row + 1, cur_col):
                    cur_coin = dp[cur_row][cur_mid] + dp[cur_mid][cur_col] \
                            + nums[cur_row] * nums[cur_mid] * nums[cur_col]
                    if cur_max_coin is None or cur_coin > cur_max_coin:
                        cur_max_coin = cur_coin
                dp[cur_row][cur_col] = cur_max_coin
        
        return dp[0][num_len - 1]


# @lc code=end