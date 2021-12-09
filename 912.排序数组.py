#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #quicksort_recursive(nums)
        #quicksort(nums)
        #merge_sort_recursive(nums)
        merge_sort(nums)
        return nums
    

def merge_sort(nums):
    merge_size = 1
    # 若本次merge_size == len(nums)
    # 说明上次prev_size = merge_size / 2 = len(nums) / 2 为整数
    # 上次的第一次合并范围为[0, prev_size - 1, 2 * prev_size - 1]
    # 即[0, len(nums) / 2 - 1, len(nums) - 1]
    # 说明上次合并就覆盖了整个数组
    # 所以merge_size == len(nums)时也不需要再进行了
    while merge_size < len(nums):
        cur_left = 0
        cur_mid = cur_left + merge_size - 1
        # 右侧范围为[cur_mid + 1, len(nums)-1]
        # 所以这里判断 右侧有 则需要归并 否则不需要
        while cur_mid < len(nums) - 1:
            cur_right = min(cur_mid + merge_size, len(nums) - 1)
            merge(nums, cur_left, cur_mid, cur_right)
            cur_left = cur_right + 1
            cur_mid = cur_left + merge_size - 1
        
        merge_size *= 2


def merge_sort_recursive(nums, left=None, right=None):
    if left is None or right is None:
        assert left is None and right is None
        left = 0
        right = len(nums) - 1
    
    if left < right:
        mid_ind = (left + right) // 2
        merge_sort_recursive(nums, left, mid_ind)
        merge_sort_recursive(nums, mid_ind + 1, right)
        merge(nums, left, mid_ind, right)


def merge(nums, left, mid, right):
    merge_list = list()
    left_ind = left
    right_ind = mid + 1
    # 两边都有的时候 判断合并
    while left_ind <= mid and right_ind <= right:
        if nums[left_ind] < nums[right_ind]:
            merge_list.append(nums[left_ind])
            left_ind += 1
        else:
            merge_list.append(nums[right_ind])
            right_ind += 1

    # 只有一边有的时候 就直接加就行了
    while left_ind <= mid:
        merge_list.append(nums[left_ind])
        left_ind += 1
    while right_ind <= right:
        merge_list.append(nums[right_ind])
        right_ind += 1
    
    # 在原来的nums上变化
    nums[left: right + 1] = merge_list


def quicksort(nums):
    stack = list()
    stack.append((0, len(nums) - 1))
    while len(stack) > 0:
        cur_left, cur_right = stack.pop()
        if cur_left < cur_right:
            cur_pivot = random_partition(nums, cur_left, cur_right)
            stack.append((cur_left, cur_pivot - 1))
            stack.append((cur_pivot + 1, cur_right))
    return nums


def quicksort_recursive(nums, left=None, right=None):
    if left is None or right is None:
        assert left is None  and right is None
        left = 0
        right = len(nums) - 1

    if left < right:
        pivot = random_partition(nums, left, right)
        quicksort_recursive(nums, left, pivot - 1)
        quicksort_recursive(nums, pivot + 1, right)


def random_partition(nums, left, right):
    # 随机范围[left, right]
    rand_ind = random.randint(left, right)
    nums[rand_ind], nums[right] = nums[right], nums[rand_ind]
    pivot_left_ind = left
    # cur_ind 范围[left, right)
    # 遍历每一个位置的值
    for cur_ind in range(left, right):
        # 如果该值小于等于pivot值 则将其放在pivot_left_ind的位置
        # pivot_left_ind加一
        # 如此保证
        # [left, pivot_left_ind)的值都小于等于pivot值
        # [pivot_left_ind, cur_ind)的值都大于pivot值
        if nums[cur_ind] <= nums[right]:
            nums[cur_ind], nums[pivot_left_ind] = nums[pivot_left_ind], nums[cur_ind]
            pivot_left_ind += 1
    # 遍历完后
    # pivot_left_ind左边的值都小于等于pivot， 其与其右边的值都大于pivot(除一开始被放在最右边的pivot值)
    # 因此 将最右边的pivot值与pivot_left_ind处的值调换
    # 如此保证了 pivot_left_ind左边小于等于pivot 自身等于pivot 右边大于pivot
    nums[pivot_left_ind], nums[right] = nums[right], nums[pivot_left_ind]
    return pivot_left_ind


# @lc code=end

