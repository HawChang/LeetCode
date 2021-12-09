#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res_list = list()
        if len(intervals) == 0:
            return res_list

        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        left = sorted_intervals[0][0]
        right = sorted_intervals[0][1]
        for cur_left, cur_right in sorted_intervals:

            if right < cur_left:
                # 与之前的区间不相交
                # 储存之前的区间
                res_list.append([left, right])
                # 更新准备之后合并的区间
                left = cur_left
                right = cur_right
            elif cur_right > right:
                # 与之前的区间 则保留两区间中 最右边的那个
                right = cur_right
        
        res_list.append([left, right])
        
        return res_list
            

# @lc code=end

