#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #return self.findTargetSumWays1(nums, target)
        return self.findTargetSumWays2(nums, target)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """
        """
        total_sum = 0
        for cur_num in nums:
            total_sum += cur_num
        
        if total_sum < target:
            return 0
        
        diff = total_sum - target
        if diff % 2 == 1:
            return 0
        
        tar_neg = diff // 2

        # dp[j]: 能否凑到j
        dp = [0 for _ in range(tar_neg + 1)]
        dp[0] = 1

        total_sum = 0

        for cur_num in nums:
            total_sum += cur_num
            prev_sum = min(total_sum, tar_neg)
            while prev_sum >= cur_num:
                dp[prev_sum] += dp[prev_sum - cur_num]
                prev_sum -= 1
        
        return dp[tar_neg]

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        """dp
        """
        total_sum = 0
        for cur_num in nums:
            total_sum += cur_num
        
        if total_sum < target:
            return 0

        # dp[j]: ????j??????
        dp = [0 for _ in range(2 * total_sum + 1)]
        zero_ind = total_sum
        dp[zero_ind] = 1
        max_sum = zero_ind
        min_sum = zero_ind

        for cur_num in nums:
            prev_sum = max_sum
            next_dp = [0 for _ in range(2 * total_sum + 1)]
            while prev_sum >= min_sum:
                next_dp[prev_sum + cur_num] += dp[prev_sum]
                next_dp[prev_sum - cur_num] += dp[prev_sum]
                prev_sum -= 1
            max_sum += cur_num
            min_sum -= cur_num
            dp = next_dp
        
        return dp[zero_ind + target]
        

# @lc code=end

