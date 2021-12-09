#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #return self.searchRange1(nums, target)
        return self.searchRange2(nums, target)

    def searchRange2(self, nums: List[int], target: int) -> List[int]:

        def search(nums, target, lower):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                # 大于小于目标值时 与普通二分查找无异
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    # 等于时 根据要求进行处理
                    # 如果要求等于目标值的第一个 那么就搜索左侧
                    # 如果要求等于目标值的最后一个 那么就搜索右侧
                    # 同时结果要更新为该次的位置 防止该位置就是第一个或者最后一个
                    ans = mid
                    if lower:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return ans
        
        return [
            search(nums, target, True),
            search(nums, target, False),
        ]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        return [
            binary_search(nums, target, "left"),
            binary_search(nums, target, "right"),
        ]

def binary_search(nums, target, type):
    # type = left or right
    left, right = 0, len(nums) - 1
    print("type: {}".format(type))
    while left <= right:
        print("left: {}, right: {}".format(left, right))
        if left == right and nums[left] == target:
            return left


        if type == "left":
            if nums[left] == target:
                return left
            mid = (left + right) // 2
        elif type == "right":
            if nums[right] == target:
                return right
            mid = (left + right + 1) // 2
        else:
            raise ValueError

        if nums[mid] == target:
            if type == "left":
                right = mid
            elif type == "right":
                left = mid
            else:
                raise ValueError
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# @lc code=end

