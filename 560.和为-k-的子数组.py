#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start

import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_len = len(nums)
        if num_len == 0:
            return 0

        res = 0
        total_sum = 0
        sum_dict = collections.defaultdict(int)
        sum_dict[0] = 1

        for cur_num in nums:
            total_sum += cur_num

            res += sum_dict[total_sum - k]

            sum_dict[total_sum] += 1
        
        return res


# @lc code=end

