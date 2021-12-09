#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import collections
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = collections.defaultdict(int)
        for cur_num in nums:
            num_count[cur_num] += 1

        num_counts = list(num_count.items())
        
        top_k_sort(num_counts, k)

        return [x[0] for x in num_counts[:k]]

    
def top_k_sort(num_counts, k):
    part_quick_sort(num_counts, k, 0, len(num_counts) - 1)


def part_quick_sort(num_counts, k, left, right):
    if left < right:
        pivot = random_pivot(num_counts, left, right)
        if k < pivot - left + 1:
            # 左边的点数比要求的k多 则看左边
            # 否则左边全部都在结果中 不用再排序了
            part_quick_sort(num_counts, k, left, pivot - 1)
        elif k > pivot - left + 1:
            # k多于左边的点数 且显然少于右边的
            # 所以要在右边找 找剩下的k-(pivot-left+1)个点
            part_quick_sort(num_counts, k - (pivot - left + 1), pivot + 1, right)


def random_pivot(num_counts, left, right):
    rand_ind = random.randint(left, right)
    num_counts[rand_ind], num_counts[right] = num_counts[right], num_counts[rand_ind]

    cur_pivot = left
    for cur_ind in range(left, right):
        if num_counts[cur_ind][1] > num_counts[right][1]:
            num_counts[cur_ind], num_counts[cur_pivot] = num_counts[cur_pivot], num_counts[cur_ind]
            cur_pivot += 1
    num_counts[cur_pivot], num_counts[right] = num_counts[right], num_counts[cur_pivot]
    return cur_pivot


# @lc code=end

