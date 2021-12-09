#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur_ind = len(nums) - 2
        while cur_ind >= 0:
            if nums[cur_ind] < nums[cur_ind + 1]:
                rep_ind = len(nums) - 1
                while nums[rep_ind] <= nums[cur_ind]:
                    rep_ind -= 1
                nums[cur_ind], nums[rep_ind] = nums[rep_ind], nums[cur_ind]
                break
            cur_ind -= 1

        left = cur_ind + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# @lc code=end

