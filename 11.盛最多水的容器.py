#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_len = len(height)
        left = 0
        right = height_len - 1

        max_water_height = 0
        max_area = 0

        while left < right:
            cur_water_height = min(height[left], height[right])
            if cur_water_height > max_water_height:
                max_area = max(max_area, cur_water_height * (right - left))
                max_water_height = cur_water_height
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# @lc code=end

