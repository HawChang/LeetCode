#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = None
        prev_sum = 0
        for cur_num in nums:
            cur_sum = prev_sum + cur_num
            if max_num is None or max_num < cur_sum:
                max_num = cur_sum
            prev_sum = max(cur_sum, 0)
        return max_num
            
# @lc code=end

