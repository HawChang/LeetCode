#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #return self.canPartition1(nums)
        #return self.canPartition2(nums)
        return self.canPartition3(nums)

    def canPartition3(self, nums: List[int]) -> bool:
        num_len = len(nums)
        if num_len < 2:
            return False

        # 遍历nums 求得目标平分的值
        total_num = 0
        for cur_num in nums:
            total_num += cur_num
        
        if total_num % 2 == 1:
            return False
        
        tar_num = total_num // 2

        # 当前能否凑齐j
        dp = [False for _ in range(tar_num + 1)]
        dp[0] = True
        
        total_sum = 0
        for cur_num in nums:
            total_sum += cur_num
            tar_sum = min(total_sum, tar_num)
            # 要倒着更新 不然遍历dp时会被本次更新的dp影响
            # 或者dp和更新的dp分开
            while tar_sum >= cur_num:
                # 之前为True的prev_sum照样True
                # 当前加上cur_num能达到的值也为True
                dp[tar_sum] |= dp[tar_sum - cur_num]
                tar_sum -= 1
            
        return dp[tar_num]

    def canPartition2(self, nums: List[int]) -> bool:
        num_len = len(nums)
        if num_len < 2:
            return False

        # 遍历nums 求得目标平分的值
        total_num = 0
        for cur_num in nums:
            total_num += cur_num
        
        if total_num % 2 == 1:
            return False
        
        tar_num = total_num // 2

        # 当前能否凑齐j
        dp = [False for _ in range(tar_num + 1)]
        dp[0] = True
        
        total_sum = 0
        for cur_num_rank in range(1, num_len + 1):
            cur_num = nums[cur_num_rank - 1]
            prev_sum = min(total_sum, tar_num)
            # 要倒着更新 不然遍历dp时会被本次更新的dp影响
            # 或者dp和更新的dp分开
            while prev_sum >= 0:
                # 之前为True的prev_sum照样True
                # 当前加上cur_num能达到的值也为True
                if dp[prev_sum] and prev_sum + cur_num <= tar_num:
                    dp[prev_sum + cur_num] = True
                prev_sum -= 1
            total_sum += cur_num
            
        return dp[tar_num]


    def canPartition1(self, nums: List[int]) -> bool:
        num_len = len(nums)
        if num_len < 2:
            return False

        # 遍历nums 求得目标平分的值
        total_num = 0
        for cur_num in nums:
            total_num += cur_num
        
        if total_num % 2 == 1:
            return False
        
        tar_num = total_num // 2

        # dp[i][j] 第i个num 是否能凑齐j
        dp = [[False for _ in range(tar_num + 1)] for _ in range(num_len + 1)]

        for cur_ind in range(num_len + 1):
            dp[cur_ind][0] = True
        
        total_sum = 0
        for cur_num_rank in range(1, num_len + 1):
            cur_num = nums[cur_num_rank - 1]
            prev_sum = 0
            while prev_sum <= total_sum and prev_sum <= tar_num:
                if dp[cur_num_rank - 1][prev_sum] == True:
                    dp[cur_num_rank][prev_sum] = True
                    if prev_sum + cur_num <= tar_num:
                        dp[cur_num_rank][prev_sum + cur_num] = True
                prev_sum += 1
            total_sum += cur_num
        
            
        return dp[num_len][tar_num]


# @lc code=end

