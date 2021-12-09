#
# @lc app=leetcode.cn id=1764 lang=python3
#
# [1764] 通过连接另一个数组的子数组得到一个数组
#

# @lc code=start

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        cur_group_ind = 0
        cur_p_pos = 0
        cur_fail_jump = gen_next(groups[cur_group_ind])
        
        can_choose_flag = False

        for cur_num in nums:
            while cur_p_pos != 0 and cur_num != groups[cur_group_ind][cur_p_pos]:
                cur_p_pos = cur_fail_jump[cur_p_pos - 1]
            
            if cur_num == groups[cur_group_ind][cur_p_pos]:
                cur_p_pos += 1
            
            if cur_p_pos == len(groups[cur_group_ind]):
                cur_group_ind += 1
                if cur_group_ind == len(groups):
                    can_choose_flag = True
                    break
                cur_p_pos = 0
                cur_fail_jump = gen_next(groups[cur_group_ind])
        
        return can_choose_flag


def gen_next(s):
    fail_jump = [0 for _ in range(len(s))]

    prefix_cmp_ind = 0

    for suffix_cmp_ind in range(1, len(s)):
        while prefix_cmp_ind != 0 and s[prefix_cmp_ind] != s[suffix_cmp_ind]:
            prefix_cmp_ind = fail_jump[prefix_cmp_ind - 1]
        
        if s[prefix_cmp_ind] == s[suffix_cmp_ind]:
            prefix_cmp_ind += 1
        
        fail_jump[suffix_cmp_ind] = prefix_cmp_ind
    
    return fail_jump


# @lc code=end

