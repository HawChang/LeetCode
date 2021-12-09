#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_max = 0
        for cur_offset, cur_jump in enumerate(nums):
            if jump_max >= cur_offset:
                cur_jump_max = cur_offset + cur_jump
                if cur_jump_max > jump_max:
                    jump_max = cur_jump_max
            else:
                return False
        return jump_max >= len(nums) - 1


# @lc code=end

