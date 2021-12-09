#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row_step = m - 1
        col_step = n -1

        total_step = row_step + col_step
        if row_step >= col_step:
            big_step = row_step
            small_step = col_step
        else:
            big_step = col_step
            small_step = row_step

        total_num = 1
        cur_ind = total_step
        while cur_ind > big_step:
            total_num *= cur_ind
            cur_ind -= 1

        cur_ind = small_step
        while cur_ind > 1:
            total_num /= cur_ind
            cur_ind -= 1
        
        return int(total_num)


# @lc code=end

