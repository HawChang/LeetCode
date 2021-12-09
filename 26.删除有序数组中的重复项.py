#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rep_ind = 0
        prev_num = None
        for cur_num in nums:
            if prev_num is not None and cur_num == prev_num:
                continue
            prev_num = cur_num
            nums[rep_ind] = cur_num
            rep_ind += 1
        nums = nums[:rep_ind]
        return rep_ind

# @lc code=end

