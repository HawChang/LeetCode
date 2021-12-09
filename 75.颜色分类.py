#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        默认为2 如果
        [2 0 2 1 1 1 0] 
        -> [2 2 2 2 2 2 2] 先全填上2
        -> [1 1 1 1 1 2 2] 统计下0和1的个数之和(作为数字1的右侧边界)，然后填上1
        -> [0 0 1 1 1 2 2] 统计下0的个数（作为数字0的右侧边界），然后填上0
        """
        #return self.sortColors1(nums)
        #return self.sortColors2(nums)
        return self.sortColors3(nums)

    def sortColors3(self, nums: List[int]) -> None:
        p0 = 0
        p2 = len(nums) - 1

        cur_i = 0
        while cur_i <= p2:
            if nums[cur_i] == 0:
                if cur_i > p0:
                    nums[cur_i], nums[p0] = nums[p0], nums[cur_i]
                p0 += 1
                cur_i += 1
            elif nums[cur_i] == 2:
                nums[cur_i], nums[p2] = nums[p2], nums[cur_i]
                p2 -= 1
            else:
                cur_i += 1

    def sortColors2(self, nums: List[int]) -> None:
        p0 = 0
        p1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1

    def sortColors1(self, nums: List[int]) -> None:
        next_zero_pos = 0
        next_one_pos  = 0
        for cur_ind, cur_num in enumerate(nums):
            nums[cur_ind] = 2
            if cur_num < 2:
                nums[next_one_pos] = 1
                next_one_pos += 1
                if cur_num == 0:
                    nums[next_zero_pos] = 0
                    next_zero_pos += 1

# @lc code=end

