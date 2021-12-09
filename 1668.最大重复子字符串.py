#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        cur_repeat_num = 0

        cur_word = word 
        fail_jump = gen_next(cur_word)
        p_pos = 0

        for cur_char in sequence:
            while p_pos != 0 and cur_char != cur_word[p_pos]:
                p_pos = fail_jump[p_pos - 1]
            
            if cur_char == cur_word[p_pos]:
                p_pos += 1
            
            # 如果匹配完当前repeat数的word  则将其变长
            # p_pos不用改
            if p_pos == len(cur_word):
                cur_word += word
                fail_jump = gen_next(cur_word)
                cur_repeat_num += 1
        
        return cur_repeat_num


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

