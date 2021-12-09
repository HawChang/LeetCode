#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        cur_min = 1
        cur_max = 1

        res = None
        
        for cur_num in nums:
            cur_min *= cur_num
            cur_max *= cur_num
            # 这里不能直接cur_max 会影响到下面的cur_min
            new_max = max(cur_max, cur_min, cur_num)
            cur_min = min(cur_max, cur_min, cur_num)
            cur_max = new_max
            
            if res is None or cur_max > res:
                res = cur_max
        
        return res


# @lc code=end

