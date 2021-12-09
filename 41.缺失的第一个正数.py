#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 将长度为N的数组转为[1,2,3,...,N]的形式
        # 遍历数组 将各位置的数放到其相应的地方
        num_size = len(nums)
        for cur_ind, cur_num in enumerate(nums):
            # 这里不需要判断 是否nums[cur_ind]是否与cur_ind + 1相等
            # nums[cur_ind] != nums[nums[cur_ind] - 1]包含了该判断
            # 且确保交换的两值不一样 避免交换的值一样 导致死循环
            while 1 <= cur_num <= num_size and cur_num != nums[cur_num - 1]:
                nums[cur_ind], nums[cur_num - 1] = nums[cur_num - 1],cur_num 
                cur_num = nums[cur_ind]
            
        # 遍历完之后 与位置不符的数 就是不对的数
        for cur_ind, cur_num in enumerate(nums):
            if cur_num != cur_ind + 1:
                return cur_ind + 1
        
        return num_size + 1

# @lc code=end

