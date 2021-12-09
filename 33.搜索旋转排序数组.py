#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]

            # 就是当前位置
            if mid_val == target:
                return mid
            
            # 如果左边有序
            if left_val <= mid_val:
                # 判断是否在左边
                if left_val <= target < mid_val:
                    return find(left, mid - 1)
                else:
                    return find(mid + 1, right)
            # 如果右边有序
            else:
                # 判断是否在右边
                if mid_val < target <= right_val:
                    return find(mid + 1, right)
                else:
                    return find(left, mid - 1)

            return -1

        return find(0, len(nums) - 1)

    def search2(self, nums: List[int], target: int) -> int:
        def find(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]

            # 就是当前位置
            if mid_val == target:
                return mid

            # 在左边区间
            if (mid_val <= right_val and (target < mid_val or right_val < target)) or left_val <= target < mid_val:
                return find(left, mid - 1)
            
            # 在右边区间
            if (left_val <= mid_val and (target < left_val or mid_val < target)) or mid_val < target <= right_val:
                return find(mid + 1, right)
            
            return -1
        return find(0, len(nums) - 1)


# @lc code=end

