#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

import random


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        quicksort(nums)
        print("sort nums: {}".format(nums))

        res_list = list()
        for cur_ind, cur_num in enumerate(nums):
            # 遍历nums 固定为第一个点
            # 与前一个相同则跳过
            if cur_ind > 0 and nums[cur_ind] == nums[cur_ind - 1]:
                continue

            right_pos = len(nums) - 1
            # 后两个点 左右两指针 遍历数组
            # 找到三数和为0
            for left_pos in range(cur_ind + 1, len(nums) - 1):
                if left_pos > cur_ind + 1 and nums[left_pos] == nums[left_pos - 1]:
                    left_pos += 1
                    continue
                
                target_num = - cur_num - nums[left_pos]
                
                while right_pos > left_pos and nums[right_pos] > target_num:
                    right_pos -= 1

                if left_pos >= right_pos:
                    break
                
                if nums[right_pos] == target_num:
                    res_list.append([nums[cur_ind], nums[left_pos], nums[right_pos]])
                    right_pos -= 1

        return res_list

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        quicksort(nums)
        print("sort nums: {}".format(nums))


        def next_val(cur_pos, direction):
            next_pos = cur_pos
            while nums[next_pos] == nums[cur_pos]:
                next_pos += direction
                if next_pos < 0 or next_pos >= len(nums):
                    return None
            return next_pos

        res_list = list()
        cur_ind = None if len(nums) == 0 else 0
        while cur_ind is not None:
            cur_num = nums[cur_ind]
        #for cur_ind, cur_num in enumerate(nums):
            # 遍历nums 固定为第一个点
            # 后两个点 左右两指针 遍历数组
            # 找到三数和为0
            left_pos = cur_ind + 1
            right_pos = len(nums) - 1
            while left_pos is not None and right_pos is not None and left_pos < right_pos:
                cur_sum = nums[left_pos] + nums[right_pos] + cur_num
                if cur_sum < 0:
                    left_pos = next_val(left_pos, 1)
                elif cur_sum == 0:
                    res_list.append([nums[cur_ind], nums[left_pos], nums[right_pos]])
                    left_pos = next_val(left_pos, 1)
                    right_pos = next_val(right_pos, -1)
                else:
                    right_pos = next_val(right_pos, -1)
            
            cur_ind = next_val(cur_ind, 1)
            
        return res_list


def quicksort(nums):
    def quick_sort_within_range(left, right):
        if left < right:
            pivot = random_pivot(nums, left, right)
            quick_sort_within_range(left, pivot - 1)
            quick_sort_within_range(pivot + 1, right)
    
    quick_sort_within_range(0, len(nums) - 1)

def random_pivot(nums, left, right):
    pivot_ind = random.randint(left, right)
    nums[pivot_ind], nums[right] = nums[right], nums[pivot_ind]
    pivot_left_ind = left

    for i in range(left, right):
        if nums[i] <= nums[right]:
            nums[i], nums[pivot_left_ind] = nums[pivot_left_ind], nums[i]
            pivot_left_ind += 1
    
    nums[pivot_left_ind], nums[right] = nums[right], nums[pivot_left_ind]
    return pivot_left_ind
    

# @lc code=end

