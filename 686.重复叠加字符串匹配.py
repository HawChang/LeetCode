#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        fail_jump = gen_next(b)

        prev_p_pos = -1
        cur_p_pos = 0

        repeat_time = 0 

        # cur_p_pos一定是单增的
        while cur_p_pos > prev_p_pos and cur_p_pos < len(b):
            repeat_time += 1
            #print("repeat time: {}, cur_p_pos: {}".format(repeat_time, cur_p_pos))
            prev_p_pos = cur_p_pos

            for cur_m_pos in range(len(a)):
                while cur_p_pos != 0 and a[cur_m_pos] != b[cur_p_pos]:
                    cur_p_pos = fail_jump[cur_p_pos - 1]
                
                if a[cur_m_pos] == b[cur_p_pos]:
                    cur_p_pos += 1
                
                if cur_p_pos == len(b):
                    break
            
        if cur_p_pos != len(b):
            repeat_time = -1

        return repeat_time


def gen_next(tar_str):
    fail_jump = [0 for _ in range(len(tar_str))]

    prefix_cmp_ind = 0
    
    for suffix_cmp_ind in range(1, len(tar_str)):
        while prefix_cmp_ind != 0 and tar_str[prefix_cmp_ind] != tar_str[suffix_cmp_ind]:
            prefix_cmp_ind = fail_jump[prefix_cmp_ind - 1]
        
        if tar_str[prefix_cmp_ind] == tar_str[suffix_cmp_ind]:
            prefix_cmp_ind += 1
        
        fail_jump[suffix_cmp_ind] = prefix_cmp_ind
    
    return fail_jump


# @lc code=end

