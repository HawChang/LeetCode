#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        s = "#{}#".format("#".join(s)) 
        print('s: {}'.format(s))

        arm_len = [0 for _ in s]
        right_most = -1
        right_center = -1

        def expand(center, arm_len_start=1):
            # 从arm_len_start开始 判断center处 回文臂长
            left = center - arm_len_start
            right = center + arm_len_start

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - 1 - center
        
        total_num = 0

        for cur_ind in range(len(s)):
            if cur_ind >= right_most:
                cur_arm_len = expand(cur_ind, 1)
            else:
                sym_ind = right_center - (cur_ind - right_center)
                cur_arm_len = right_most - cur_ind
                sym_arm_len = arm_len[sym_ind]
                if cur_arm_len == sym_arm_len:
                    cur_arm_len = expand(cur_ind, cur_arm_len + 1)
                else:
                    cur_arm_len = min(cur_arm_len, sym_arm_len)
            
            arm_len[cur_ind] = cur_arm_len
            total_num += (cur_arm_len + 1) // 2

            cur_right_most = cur_arm_len + cur_ind
            if cur_right_most > right_most:
                right_most = cur_right_most
                right_center = cur_ind
        
        return total_num


# @lc code=end