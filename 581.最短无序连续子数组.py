#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #return self.findUnsortedSubarray1(nums)
        return self.findUnsortedSubarray2(nums)

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        """左右遍历同时进行 且不需要保存所有 分别保存leftmax和rightmin就行了
        """
        num_len = len(nums)
        if num_len == 0:
            return 0

        left_max = nums[0]
        right_min = nums[-1]

        right_end = None
        left_start = None
    
        for cur_ind in range(1, num_len):
            if left_max > nums[cur_ind]:
                right_end = cur_ind
            else:
                left_max = nums[cur_ind]
            
            sym_ind = num_len - 1 - cur_ind
            if right_min < nums[sym_ind]:
                left_start = sym_ind
            else:
                right_min = nums[sym_ind]
        
        return 0 if left_start is None else right_end - left_start + 1

    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        """左右两遍 分别看leftmax和rightmin
        """
        num_len = len(nums)
        if num_len == 0:
            return 0

        left_max = [0 for _ in range(num_len)]
        right_min = [0 for _ in range(num_len)]

        left_max[0] = nums[0]
        right_min[num_len - 1] = nums[num_len - 1]

        for cur_ind in range(1, num_len):
            left_max[cur_ind] = max(left_max[cur_ind - 1], nums[cur_ind])
            sym_ind = num_len - 1 - cur_ind
            right_min[sym_ind] = min(right_min[sym_ind + 1], nums[sym_ind])
        
        left = None
        right = None
        # 不用分开找最左最右 一次性遍历 找到第一个和最后一个left_max > right_min的就可以了
        for cur_ind in range(num_len):
            if right_min[cur_ind] < left_max[cur_ind]:
                if left is None:
                    left = cur_ind
                right = cur_ind
        
        #print("left: {}, right: {}".format(left, right))
        return 0 if left is None else right - left + 1

# @lc code=end

