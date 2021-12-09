#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dec_stack = list()
        res = [0 for _ in temperatures]
        for cur_ind, cur_temp in enumerate(temperatures):
            while len(dec_stack) > 0 and dec_stack[-1][1] < cur_temp:
                prev_ind, prev_temp = dec_stack.pop()
                res[prev_ind] = cur_ind - prev_ind
            dec_stack.append((cur_ind, cur_temp))
        
        return res




# @lc code=end

