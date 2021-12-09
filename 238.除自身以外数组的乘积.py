#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        ans = [1 for _ in range(num_len)]

        # 当前ans[i]: i左侧乘积
        total_left = 1
        for cur_ind in range(1, num_len):
            total_left *= nums[cur_ind - 1]
            ans[cur_ind] = total_left

        total_right = 1
        for cur_ind in range(1, num_len):
            total_right *= nums[num_len - cur_ind]
            ans[num_len - cur_ind - 1] *= total_right
        
        return ans


# @lc code=end

