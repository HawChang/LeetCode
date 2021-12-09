#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        # 以较短的数组为nums1 之后遍历nums1中i的位置
        if nums1_length > nums2_length:
            return self.findMedianSortedArrays(nums2, nums1)

        # 二分查找切分点时 为处理边界条件 即ind为0或列表长度时
        # 设置一个无限大的值 因为列表中的数最大为1e6 所以这里设置1e7就可以了
        infinity = 1e7
        
        # 两列表的切分点之和 应该等于median_ind_sum
        # 则：
        # 1. 当两列表长度之和为偶数时，两列表的左侧长度等于右侧长度
        # 2. 当两列表长度之和为奇数时，两列表的左侧长度等于右侧长度加1
        median_ind_sum = (nums1_length + nums2_length + 1) // 2

        # 在nums1上二分查找i的位置
        # nums1有m个数 切分位置有m+1个，
        # 包括数组开始之前和数组结尾之后
        left, right = 0, len(nums1)

        while left <= right:
            # split_i示在当前索引之前划分
            # 因此nums1左侧范围是[0, split_i - 1] nums2左侧范围是[0, split_j - 1]
            # 也表示了nums1 nums2左侧有多少个数
            split_i = (left + right) // 2
            split_j = median_ind_sum - split_i

            # 如果切分在数组开始之前 则左侧没有任何数 将两数组左侧最大值都设为负无穷
            nums1_left = -infinity if split_i == 0 else nums1[split_i - 1]
            nums2_left = -infinity if split_j == 0 else nums2[split_j - 1]

            # 如果切分在数组结尾之后 则右侧没有任何数 将两数组右侧最小值设为正无穷
            nums1_right = infinity if split_i == len(nums1) else nums1[split_i]
            nums2_right = infinity if split_j == len(nums2) else nums2[split_j]

            # 判断当前切分split_i是否成功
            if nums1_left > nums2_right:
                right = split_i - 1
            elif nums2_left > nums1_right:
                left = split_i + 1
            else:
                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)
                #print("left_max: {}, right_min: {}".format(left_max, right_min))

                if (nums1_length + nums2_length) % 2 == 0:
                    return (left_max + right_min) / 2.0
                else:
                    return left_max
        
        return None

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        if nums1_length > nums2_length:
            return self.findMedianSortedArrays2(nums2, nums1)
        
        # 两列表的切分点之和 应该等于median_ind_sum
        # 则：
        # 1. 当两列表长度之和为偶数时，两列表的左侧长度等于右侧长度
        # 2. 当两列表长度之和为奇数时，两列表的左侧长度等于右侧长度加1
        median_ind_sum = (nums1_length + nums2_length + 1) // 2

        # 二分查找切分点时 为处理边界条件 即ind为0或列表长度时
        # 设置一个无限大的值 因为列表中的数最大为1e6 所以这里设置1e7就可以了
        infinity = 1e7
        
        # 二分查找满足条件的切分点
        left_ind = 0
        right_ind = nums1_length
        
        # 最终的中位数值
        median = None
        
        while left_ind <= right_ind:
            # 当前二分查找范围里的中间索引
            cur_nums1_ind = (left_ind + right_ind) // 2
            # 另一个数组对应的索引值
            cur_nums2_ind = median_ind_sum - cur_nums1_ind

            # 当前索引下 两个列表左侧和右侧 共四个值
            nums1_left_max = -infinity if cur_nums1_ind == 0 else nums1[cur_nums1_ind - 1]
            nums2_left_max = -infinity if cur_nums2_ind == 0 else nums2[cur_nums2_ind - 1]
            nums1_right_min = infinity if cur_nums1_ind == nums1_length else nums1[cur_nums1_ind]
            nums2_right_min = infinity if cur_nums2_ind == nums2_length else nums2[cur_nums2_ind]

            # 当nums1[cur_nums1_ind - 1] <= nums2[cur_nums2_ind]
            # 且nums2[cur_nums2_ind - 1] <= nums1[cur_nums1_ind]时：
            # 说明左侧数都小于右侧 找到了目标切分
            # 这里要注意数组的边界 即cur_nums1_ind为0或为nums1_length时的情况
            if nums1_left_max <= nums2_right_min:
                if nums2_left_max <= nums1_right_min:
                    # 找到目标切分后 根据两数组总长度分奇偶两种情况求中位数
                    left_max = max(nums1_left_max, nums2_left_max)
                    if (nums1_length + nums2_length) % 2 == 0:
                        # 当总长度为偶数时
                        # 中位数为左侧最大值和右侧最小值的平均数
                        right_min = min(nums1_right_min, nums2_right_min)
                        median = (left_max + right_min) / 2.0
                    else:
                        # 当长度为奇数时
                        # 中位数即左侧最大值 因为目标切分会使左侧长度比右侧多一个
                        median = left_max
                    break
                left_ind += 1
            else:
                right_ind -= 1
        
        return median
        
        
# @lc code=end

