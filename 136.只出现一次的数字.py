#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur_res = 0
        for cur_num in nums:
            cur_res ^= cur_num
        return cur_res
# @lc code=end

