#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for cur_ind, cur_num in enumerate(nums):
            tar_num = target - cur_num
            if tar_num in num_dict:
                return [num_dict[tar_num], cur_ind]
            
            num_dict[cur_num] = cur_ind
        
        return None


# @lc code=end

