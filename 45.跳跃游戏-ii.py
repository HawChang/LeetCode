#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        prev_jump_max = 0
        next_jump_max = 0
        step = 0

        for cur_offset, cur_jump in enumerate(nums):
            if cur_offset > prev_jump_max:
                prev_jump_max = next_jump_max
                step += 1
            cur_jump_max = cur_offset + cur_jump
            if cur_jump_max > next_jump_max:
                next_jump_max = cur_jump_max
        
        return step



# @lc code=end

