#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start , new_end = newInterval
        res_list = list()
        cur_ind = 0
        # 区间分三种情况
        # 1. 在新增区间的左边 且无交叉
        # 2. 在新增区间的右边 且无交叉
        # 3. 与新增区间相交、交叉、覆盖等情况，这些情况，都是取两区间最左的左边界和最右的右边界
        while cur_ind < len(intervals):
            cur_start, cur_end = intervals[cur_ind]
            # 完全在左边
            if cur_end < new_start:
                res_list.append((cur_start, cur_end))
            # 完全在右边 在右边的话 就直接跳出循环了
            elif cur_start > new_end:
                break
            # 有交叉
            else:
                # 选最左的左边界
                if cur_start < new_start:
                    new_start = cur_start
                # 选最右的右边界
                if cur_end > new_end:
                    new_end = cur_end
            cur_ind += 1
        # 循环完后，表示当前新增区间已调整好 且cur_ind已指向原区间列表中处于新增区间右边的区间了
        # 直接加上新增区间 和 原列表中剩下的区间 
        res_list.append([new_start, new_end])
        res_list.extend(intervals[cur_ind:])
        return res_list

# @lc code=end

