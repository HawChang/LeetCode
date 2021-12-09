#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev_num = None
        prev_count = 0

        for cur_num in nums:
            if prev_num is None:
                prev_num = cur_num
                prev_count = 1
            elif prev_num != cur_num:
                prev_count -= 1
                if prev_count == 0:
                    prev_num = None
            else:
                prev_count += 1

        return prev_num

# @lc code=end

