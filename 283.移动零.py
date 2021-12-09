#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #self.moveZeroes1(nums)
        self.moveZeroes2(nums)

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_ind = 0
        for cur_ind, cur_num in enumerate(nums):
            if cur_num != 0:
                nums[cur_ind], nums[swap_ind] = nums[swap_ind], nums[cur_ind]
                swap_ind += 1

    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur_ind = 0
        for cur_num in nums:
            if cur_num != 0:
                nums[cur_ind] = cur_num
                cur_ind += 1
        
        nums[cur_ind:] = [0] * (len(nums) - cur_ind)


# @lc code=end

