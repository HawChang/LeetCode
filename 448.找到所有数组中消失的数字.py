#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #return self.findDisappearedNumbers1(nums)
        return self.findDisappearedNumbers2(nums)

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        for cur_num in nums:
            cur_num %= num_len
            nums[cur_num - 1] += num_len
        
        return [i + 1 for i, x in enumerate(nums) if x <= num_len]

    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        for cur_ind in range(len(nums)):
            has_prev_ind = False
            while cur_ind < len(nums) and cur_ind + 1 != nums[cur_ind]:
                next_ind = nums[cur_ind] - 1
                if has_prev_ind:
                    nums[cur_ind] = cur_ind + 1
                else:
                    has_prev_ind = True
                
                cur_ind = next_ind
        
        diff_res = list()
        for cur_ind in range(len(nums)):
            if cur_ind + 1 != nums[cur_ind]:
                diff_res.append(cur_ind + 1)
        
        return diff_res


# @lc code=end

