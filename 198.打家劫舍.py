#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        #return self.rob1(nums)
        return self.rob2(nums)

    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # dp[i]:第i家时能抢到的最大的钱
        dp = [0 for _ in range(len(nums) + 1)]

        dp[0] = 0
        dp[1] = nums[0]

        for cur_ind in range(2, len(nums) + 1):
            # 当前cur_ind不打劫能拿到的金额
            # 两种情况
            # 前一家偷了 这一家不偷
            # 前一家的没偷 偷这一家
            dp[cur_ind] = max(
                dp[cur_ind - 1],
                dp[cur_ind - 2] + nums[cur_ind - 1],
                )
        
        return dp[len(nums)]

    def rob1(self, nums: List[int]) -> int:
        # dp[0] no_rob dp[1] rob
        dp = [[0 for _ in range(len(nums) + 1)] for _ in range(2)]

        dp[0][0] = 0
        dp[1][0] = 0

        for cur_ind, cur_num in enumerate(nums):
            # 当前cur_ind不打劫能拿到的金额
            dp[0][cur_ind + 1] = max(dp[0][cur_ind], dp[1][cur_ind])
            # 当前cur_ind打劫能拿到的金额
            dp[1][cur_ind + 1] = dp[0][cur_ind] + cur_num
        
        return max(dp[0][len(nums)], dp[1][len(nums)])

# @lc code=end

