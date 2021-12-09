#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.kth_big_quicksort(nums, k)
        #self.stack_quicksort(nums)
        print("nums: {}".format(nums))
        return nums[len(nums) - k]
    
    def kth_big_quicksort(self, nums: List[int], k:int):
        tar_ind = len(nums) - k
        stack = list()
        stack.append((0, len(nums) - 1))
        while len(stack) > 0:
            cur_left, cur_right = stack.pop()
            if cur_left < cur_right:
                pivot = self.partition(nums, cur_left, cur_right)
                if pivot == tar_ind:
                    break
                elif pivot > tar_ind:
                    stack.append((cur_left, pivot - 1))
                else: 
                    stack.append((pivot + 1, cur_right))

    def stack_quicksort(self, nums: List[int]):
        """非递归快排
        """
        stack = list()
        stack.append((0, len(nums) - 1))
        while len(stack) > 0:
            cur_left, cur_right = stack.pop()
            if cur_left < cur_right:
                pivot = self.partition(nums, cur_left, cur_right)
                stack.append((cur_left, pivot - 1))
                stack.append((pivot + 1, cur_right))

    def quicksort(self, nums: List[int]):
        """递归快排
        """
        # 排序范围[left, right]
        self.range_quicksort(nums, 0, len(nums) - 1)
    
    def range_quicksort(self, nums: List[int], left, right):
        # 排序范围[left, right]
        if left < right:
            # 随机选取一个标杆 然后将标杆放入数组某位置
            # 标杆左侧均小于等于标杆 右侧均大于标杆
            # 返回标杆所处位置
            pivot = self.partition(nums, left, right)
            # 然后对标杆左右两侧重复同样操作
            self.range_quicksort(nums, left, pivot - 1)
            self.range_quicksort(nums, pivot + 1, right)
        
    def partition(self, nums: List[int], left, right):
        # 随机选出一个位置
        rand_ind = random.randint(left, right)
        # 将该标杆放到数组最右侧
        nums[rand_ind], nums[right] = nums[right], nums[rand_ind]
        # 初始化当前标杆位置
        pivot_ind = left

        # 遍历当前给定的范围[left, right)
        # 注意不包括right 因为right就是标杆 可以忽略 最后标杆会跟pivot_ind调换
        for cur_ind in range(left, right):
            # 当值小于标杆时
            if nums[cur_ind] <= nums[right]:
                # 该值与当前pivot_ind调换
                nums[cur_ind], nums[pivot_ind] = nums[pivot_ind], nums[cur_ind]
                # 并更新pivot_ind位置
                # 注意 因为从左到右遍历时 每遇到小于大于标杆值的数 pivot_ind都会更新
                # 所以pivot_ind要不比标杆值大 要不就是当前遍历到的值
                # 可以保证pivot_ind左侧的都小于等于标杆值
                pivot_ind += 1
        
        # 遍历完后，当前pivot_ind左侧的值都小于等于标杆值
        # 而pivot_ind要不就是大于标杆值 要不就是指向了right位置
        # 将标杆值与pivot_ind调换 可以在两种情况下都构造出符合要求的数组
        nums[right], nums[pivot_ind] = nums[pivot_ind], nums[right]
        #print("nums[{},{}]: {}".format(left, right, nums[left:right+1]))
        #print("pivot value: {}, ind: {}".format(pivot_value, pivot_ind))
        # 返回调整后 标杆值在数组中的位置
        return pivot_ind



# @lc code=end

