#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        val_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        s_size = len(s)
        total = 0
        prev_val = val_dict[s[0]]
        for cur_ind in range(1, s_size):
            cur_val = val_dict[s[cur_ind]]
            if prev_val < cur_val:
                prev_val *= -1
            
            total += prev_val
            prev_val = cur_val
        
        total += prev_val
        return total


# @lc code=end

