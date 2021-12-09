#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #return self.lengthOfLIS1(nums)
        return self.lengthOfLIS2(nums)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # dp[len] = num: 长为len的序列 最后一个数最小是多少
        dp = list()

        # dp是递增的 即如果长为3的递增序列的最后一个数 一定大于长为2的递增序列的最后一个数

        # 遍历每一个数
        # 需要找到该数可以加在哪个序列
        # 如果dp[i] < cur_num < dp[i+1]
        # 则dp[i+1]将被更新为cur_num
        # 而其他的不会变
        for cur_num in nums:
            # 找到dp中的位置i
            if len(dp) == 0 or cur_num > dp[-1]:
                dp.append(cur_num)
            else:
                left = 0
                right = len(dp) - 1
                tar_pos = right
                # 找第一个大于cur_num的值
                while left <= right:
                    mid = (left + right) // 2
                    # 当前mid值大于cur_num
                    # 更新tar_pos 因为mid一定比right在前面
                    if cur_num < dp[mid]:
                        tar_pos = mid
                        right = mid - 1
                    elif cur_num > dp[mid]:
                        left = mid + 1
                    else:
                        tar_pos = mid
                        break
                dp[tar_pos] = cur_num
        
        return len(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        # dp[i]: 以nums[i]结尾的最长递增子序列
        dp = list()

        max_len = 0

        for cur_ind, cur_num in enumerate(nums):
            max_prev_len = 0
            for prev_ind in range(cur_ind):
                if nums[prev_ind] < cur_num and max_prev_len < dp[prev_ind]:
                    max_prev_len = dp[prev_ind]
            
            cur_max_len = max_prev_len + 1
            
            dp.append(cur_max_len)
            if max_len < cur_max_len:
                max_len = cur_max_len
        
        return max_len


# @lc code=end

