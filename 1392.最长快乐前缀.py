#
# @lc app=leetcode.cn id=1392 lang=python3
#
# [1392] 最长快乐前缀
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        fail_jump = gen_next(s)
        return s[:fail_jump[len(s) - 1]]


def gen_next(tar_str):
    fail_jump = [0 for _ in range(len(tar_str))]
    prefix_cmp_ind = 0
    for suffix_cmp_ind in range(1, len(tar_str)):
        while prefix_cmp_ind != 0 and tar_str[prefix_cmp_ind] != tar_str[suffix_cmp_ind]:
            prefix_cmp_ind = fail_jump[prefix_cmp_ind - 1]

        if tar_str[prefix_cmp_ind] == tar_str[suffix_cmp_ind]:
            prefix_cmp_ind += 1
        
        fail_jump[suffix_cmp_ind] = prefix_cmp_ind
    
    #print(fail_jump)
    
    return fail_jump
        



# @lc code=end

